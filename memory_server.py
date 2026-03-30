"""
Claude Working Memory Server
Render-hosted Flask service providing Claude with persistent session context.
Endpoints:
  GET  /memory              — fetch working memory (startup read)
  POST /memory?key=...      — write session summary
  GET  /memory/sessions     — last 10 session logs
  GET  /memory/projects     — project state snapshot
  POST /memory/projects?key=... — update project state
  GET  /health              — health check
"""

import os
import json
from datetime import datetime, timezone
from flask import Flask, request, jsonify

app = Flask(__name__)

MEMORY_DIR = "/mnt/data/claude_memory"
WORKING_MEMORY_FILE = f"{MEMORY_DIR}/working_memory.json"
SESSION_LOG_FILE = f"{MEMORY_DIR}/session_log.json"
PROJECT_STATE_FILE = f"{MEMORY_DIR}/project_state.json"
WRITE_KEY = os.environ.get("CLAUDE_MEMORY_KEY", "changeme")
MAX_SESSIONS = 10

def ensure_dirs():
    os.makedirs(MEMORY_DIR, exist_ok=True)

def load_json(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def check_key():
    key = request.args.get("key") or request.headers.get("X-Memory-Key")
    return key == WRITE_KEY

# ── Health ────────────────────────────────────────────────────────────────────

@app.route("/health")
def health():
    return jsonify({"status": "ok", "time": datetime.now(timezone.utc).isoformat()})

# ── Working Memory ────────────────────────────────────────────────────────────

@app.route("/memory", methods=["GET"])
def get_memory():
    ensure_dirs()
    memory = load_json(WORKING_MEMORY_FILE, {
        "last_updated": None,
        "current_focus": "No session recorded yet.",
        "active_projects": [],
        "last_session_summary": "",
        "open_threads": [],
        "notes": ""
    })
    sessions = load_json(SESSION_LOG_FILE, [])
    memory["recent_sessions"] = sessions[-3:] if sessions else []
    return jsonify(memory)

@app.route("/memory", methods=["POST"])
def post_memory():
    if not check_key():
        return jsonify({"error": "Unauthorized"}), 401
    ensure_dirs()
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No JSON body"}), 400

    # Update working memory
    memory = load_json(WORKING_MEMORY_FILE, {})
    memory.update(data)
    memory["last_updated"] = datetime.now(timezone.utc).isoformat()
    save_json(WORKING_MEMORY_FILE, memory)

    # Append to session log
    sessions = load_json(SESSION_LOG_FILE, [])
    sessions.append({
        "timestamp": memory["last_updated"],
        "summary": data.get("last_session_summary", ""),
        "focus": data.get("current_focus", "")
    })
    sessions = sessions[-MAX_SESSIONS:]
    save_json(SESSION_LOG_FILE, sessions)

    return jsonify({"status": "ok", "updated": memory["last_updated"]})

# ── Session Log ───────────────────────────────────────────────────────────────

@app.route("/memory/sessions", methods=["GET"])
def get_sessions():
    ensure_dirs()
    sessions = load_json(SESSION_LOG_FILE, [])
    return jsonify({"sessions": sessions, "count": len(sessions)})

# ── Project State ─────────────────────────────────────────────────────────────

@app.route("/memory/projects", methods=["GET"])
def get_projects():
    ensure_dirs()
    projects = load_json(PROJECT_STATE_FILE, {})
    return jsonify(projects)

@app.route("/memory/projects", methods=["POST"])
def post_projects():
    if not check_key():
        return jsonify({"error": "Unauthorized"}), 401
    ensure_dirs()
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No JSON body"}), 400
    projects = load_json(PROJECT_STATE_FILE, {})
    projects.update(data)
    projects["last_updated"] = datetime.now(timezone.utc).isoformat()
    save_json(PROJECT_STATE_FILE, projects)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
