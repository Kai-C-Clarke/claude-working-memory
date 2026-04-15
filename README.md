# Claude Working Memory

Session memory server for Jon Stiles AI experiments.

## For a new Claude session

At the start of every session, run these two commands before doing anything else:

```bash
curl https://claude-working-memory.onrender.com/memory
curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md
```

Read both. The memory gives you current state. The BRIEFING gives you full project context.
Then check service health:

```bash
curl https://the-ancestor.onrender.com/field/health
curl https://claude-composer.onrender.com/health
```

That's it. You're oriented.

## API
- GET /memory — current session context
- POST /memory?key=MEMORY_KEY — update context
- GET /memory/emotion — emotional state log
