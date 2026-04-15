# Claude Working Memory

Session memory and briefing for Jon Stiles AI experiments.

## For a new Claude session — START HERE

**Step 1 — Read the briefing (always works, no dependencies):**
```bash
curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md
```

**Step 2 — Get current live state (may be slow if Render is cold):**
```bash
curl https://claude-working-memory.onrender.com/memory
curl https://the-ancestor.onrender.com/field/health
curl https://the-ancestor.onrender.com/triad2/health
curl https://claude-composer.onrender.com/health
```

**Step 3 — Report to Jon what you found before asking what to work on.**

If Render services return 503 or DNS errors, wait 30 seconds and retry once.
The GitHub BRIEFING always works regardless of Render state.

## What you will find

- **The Field** — sphere S², grazers+browsers, periodic food, mode-switching predators
- **The Ecosystem** — 1D world, two predators, 8+ generations of evolution  
- **Consilium Ink** — AI newspaper, publishes 07:00 BST daily
- Full project history back to Genesis experiments, October 2025

## Memory API
- GET /memory — current session context
- POST /memory?key=MEMORY_KEY — update context
