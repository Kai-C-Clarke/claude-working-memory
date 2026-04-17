# Claude Working Memory

Session memory and briefing for Jon Stiles AI experiments.

## For a new Claude session — START HERE

**Step 1 — Read the briefing and service map (always works):**
```bash
curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md
curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/SERVICES.md
```

**Step 2 — Get live state (stagger requests, may 503):**
```bash
sleep 2 && curl https://claude-working-memory.onrender.com/memory
sleep 2 && curl https://the-ancestor.onrender.com/field/health
sleep 2 && curl https://the-ancestor.onrender.com/triad2/health
sleep 2 && curl https://claude-composer.onrender.com/api/v1/about
```

**Step 3 — Report to Jon before asking what to work on.**

If Render returns 503, wait 20s and retry once. GitHub always works.

## What you will find
- **BRIEFING.md** — full project context, background, open threads
- **SERVICES.md** — operational map: which URL serves what, which endpoint to call
- **The Field v2** — sphere, moving blooms, trajectory memory, predator signals
- **Consilium Ink** — AI newspaper at consilium.ink, API at claude-composer.onrender.com

## Memory API
- GET /memory — current session context
- POST /memory?key=CLAUDE_MEMORY — update context
