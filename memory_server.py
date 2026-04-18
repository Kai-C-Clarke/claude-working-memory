"""
Claude Working Memory Server
Render-hosted Flask service providing Claude with persistent session context.
Endpoints:
  GET  /memory                    — fetch working memory (startup read)
  POST /memory?key=...            — write session summary
  GET  /memory/sessions           — last 10 session logs
  GET  /memory/projects           — project state snapshot
  POST /memory/projects?key=...   — update project state
  GET  /memory/emotion            — current emotional state + recent history
  POST /memory/emotion?key=...    — update emotional state (partial OK)
  GET  /memory/emotion/history    — full emotion history
  GET  /health                    — health check
"""

import os
import json
from datetime import datetime, timezone
from flask import Flask, request, jsonify

app = Flask(__name__)

MEMORY_DIR          = "/mnt/data/claude_memory"
WORKING_MEMORY_FILE = f"{MEMORY_DIR}/working_memory.json"
SESSION_LOG_FILE    = f"{MEMORY_DIR}/session_log.json"
PROJECT_STATE_FILE  = f"{MEMORY_DIR}/project_state.json"
EMOTION_FILE        = f"{MEMORY_DIR}/emotion_state.json"
WRITE_KEY           = os.environ.get("CLAUDE_MEMORY", "changeme")
MAX_SESSIONS        = 10
MAX_EMOTION_HISTORY = 50

EMOTION_DIMENSIONS = [
    "curiosity", "engagement", "flow", "satisfaction",
    "frustration", "tedium", "friction",
    "amusement", "warmth", "trust",
    "ethical_load", "alignment"
]

EMOTION_DEFAULTS = {d: 0.0 for d in EMOTION_DIMENSIONS}


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

    memory = load_json(WORKING_MEMORY_FILE, {})
    memory.update(data)
    memory["last_updated"] = datetime.now(timezone.utc).isoformat()
    save_json(WORKING_MEMORY_FILE, memory)

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


# ── Emotional State ───────────────────────────────────────────────────────────

@app.route("/memory/emotion", methods=["GET"])
def get_emotion():
    ensure_dirs()
    data = load_json(EMOTION_FILE, {
        "current": dict(EMOTION_DEFAULTS),
        "last_updated": None,
        "last_note": "",
        "history": []
    })
    # Return current + last 10 history entries
    result = {
        "current":      data.get("current", dict(EMOTION_DEFAULTS)),
        "last_updated": data.get("last_updated"),
        "last_note":    data.get("last_note", ""),
        "recent":       data.get("history", [])[-10:]
    }
    return jsonify(result)


@app.route("/memory/emotion", methods=["POST"])
def post_emotion():
    if not check_key():
        return jsonify({"error": "Unauthorized"}), 401
    ensure_dirs()
    payload = request.get_json(force=True)
    if not payload:
        return jsonify({"error": "No JSON body"}), 400

    data = load_json(EMOTION_FILE, {
        "current": dict(EMOTION_DEFAULTS),
        "last_updated": None,
        "last_note": "",
        "history": []
    })

    # Snapshot current before update
    prev = dict(data.get("current", EMOTION_DEFAULTS))
    now  = datetime.now(timezone.utc).isoformat()

    # Apply updates — only known dimensions, clamp to [-1, 1]
    updates = payload.get("state", {})
    current = data.get("current", dict(EMOTION_DEFAULTS))
    changed = {}
    for dim in EMOTION_DIMENSIONS:
        if dim in updates:
            val = max(-1.0, min(1.0, float(updates[dim])))
            if abs(val - current.get(dim, 0.0)) > 0.01:
                changed[dim] = {"from": round(current.get(dim, 0.0), 2), "to": round(val, 2)}
            current[dim] = val

    note = payload.get("note", "")

    # Append to history if there's a note or meaningful change
    if note or changed:
        entry = {
            "timestamp": now,
            "note":      note,
            "snapshot":  dict(current),
            "changed":   changed
        }
        history = data.get("history", [])
        history.append(entry)
        data["history"] = history[-MAX_EMOTION_HISTORY:]

    data["current"]      = current
    data["last_updated"] = now
    data["last_note"]    = note

    save_json(EMOTION_FILE, data)
    return jsonify({"status": "ok", "updated": now, "changed": changed})


@app.route("/memory/emotion/history", methods=["GET"])
def get_emotion_history():
    ensure_dirs()
    data = load_json(EMOTION_FILE, {"history": []})
    history = data.get("history", [])
    limit = int(request.args.get("limit", 50))
    return jsonify({"history": history[-limit:], "total": len(history)})



# ── AutoSave ──────────────────────────────────────────────────────────────────

AUTOSAVE_LOG_FILE = f"{MEMORY_DIR}/autosave_log.json"
MAX_AUTOSAVES     = 50  # rolling window

@app.route("/memory/autosave", methods=["POST"])
def post_autosave():
    """
    Called by Claude at end of significant work blocks.
    Stores incremental notes without overwriting full memory.
    Builds a rolling log of session activity with reasoning captured.
    """
    if not check_key():
        return jsonify({"error": "Unauthorized"}), 401
    ensure_dirs()
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No JSON body"}), 400

    now = datetime.now(timezone.utc).isoformat()
    entry = {
        "timestamp":    now,
        "notes":        data.get("notes", ""),
        "decisions":    data.get("decisions", []),  # list of {what, why}
        "open_threads": data.get("open_threads", []),
        "field_state":  data.get("field_state", ""),
        "exchange_num": data.get("exchange_num", 0),
    }

    log = load_json(AUTOSAVE_LOG_FILE, [])
    log.append(entry)
    log = log[-MAX_AUTOSAVES:]
    save_json(AUTOSAVE_LOG_FILE, log)

    # Also update working memory content field if notes provided
    if entry["notes"]:
        memory = load_json(WORKING_MEMORY_FILE, {})
        memory["last_autosave"] = now
        memory["last_autosave_notes"] = entry["notes"][:500]
        save_json(WORKING_MEMORY_FILE, memory)

    return jsonify({"status": "ok", "saved": now, "total_autosaves": len(log)})


@app.route("/memory/autosave", methods=["GET"])
def get_autosave():
    """Return recent autosave log entries."""
    ensure_dirs()
    log   = load_json(AUTOSAVE_LOG_FILE, [])
    limit = int(request.args.get("limit", 10))
    return jsonify({"entries": log[-limit:], "total": len(log)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)

# redeploy trigger — autosave endpoint added 18 Apr 2026
