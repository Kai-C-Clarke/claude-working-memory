# Claude Working Memory

Lightweight Flask service providing Claude with persistent session context across conversations.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/memory` | Fetch working memory + last 3 sessions (startup read) |
| POST | `/memory?key=...` | Write session summary |
| GET | `/memory/sessions` | Last 10 session logs |
| GET | `/memory/projects` | Project state snapshot |
| POST | `/memory/projects?key=...` | Update project state |
| GET | `/health` | Health check |

## Deploy

1. Create Render web service pointing to this repo
2. Set env var `CLAUDE_MEMORY_KEY` to a secret value
3. Attach a 1GB persistent disk at `/mnt/data`

## Purpose

Keeps Claude's session context lean and fast — a single GET at startup 
returns everything needed to continue work without wading through 
Consilium's 750+ mind cycle entries.
