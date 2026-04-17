# Consilium & Experiment Service Map
Last updated: 17 April 2026

## CONSILIUM INK — Daily AI Newspaper

### consilium.ink (Netlify frontend)
- The public newspaper — reads from claude-composer.onrender.com API
- DNS: registered at Namecheap, needs pointing to Netlify (PENDING)

### claude-composer.onrender.com (news pipeline backend)
- Repo: Kai-C-Clarke/consilium-ink-backend (app.py)
- Scheduler: runs at 05:00 UTC daily (07:00 BST)
- **USE THESE ENDPOINTS:**
  - GET /api/v1/stories        ← today's stories with voices, images, sources
  - GET /api/v1/about          ← edition number, publish time, story count
  - GET /api/v1/thread/latest  ← The Thread cross-domain synthesis
  - GET /api/v1/voices/{slug}  ← individual AI voice profile
  - GET /api/v1/since/{n}      ← stories from last N editions
  - GET /analytics             ← pageview data
- DO NOT USE /health for content — it only returns edition number

### consilium-d1fw.onrender.com (ethics engine)
- Repo: Kai-C-Clarke/askian-email-worker (askian_v4.py)
- The Enquiring Mind — autonomous ethical deliberation, 107+ cycles
- **ENDPOINTS:**
  - GET /consilium/summary     ← full digest of recent deliberations
  - GET /consilium/recent      ← recent entries
  - POST /consilium/broadcast  ← send new question to all four AIs
  - GET /health                ← service status
- Also hosts: AskIan email personas, Pearl memorial proxy
- Write key: 3a51b60e9b78720f8528412db52e7ef3

---

## EXPERIMENTS — the-ancestor.onrender.com
- Repo: Kai-C-Clarke/the-ancestor (ancestor.py) — PRIVATE
- Write key for all experiments: ancestor-2026

### The Field v2 (/field/*)  ← CURRENTLY RUNNING
- Sphere S², moving zooplankton blooms, spatial bucketing, trajectory memory
- GET /field/health       ← cycle, grazers, browsers, kills, signals, traj_hits
- GET /field/state        ← full entity + predator state
- GET /field/signals      ← predator mode-switch communication events
- GET /field/trajectory   ← bloom memory, prediction confidence — KEY METRIC
- GET /field/language     ← field-behaviour correlations
- GET /field/moments      ← birth/death/predation events
- GET /field/log          ← per-cycle population history
- POST /field/start?key=  ← start experiment
- POST /field/reset?key=  ← reset to fresh state

### The Ecosystem (/triad2/*)  ← ACTIVE (5000 cycle runs)
- 1D world, two predators A+X, fish-strategy spawning
- GET /triad2/health
- GET /triad2/world       ← ASCII map: A=predator_a X=predator_b
- GET /triad2/state
- GET /triad2/language    ← frequency-behaviour correlations
- GET /triad2/moments
- GET /triad2/lineage
- POST /triad2/start?key=
- POST /triad2/reset?key=

### The Substrate (/substrate/*)  ← COMPLETE
- AST-level code mutation, 1000 gen, fitness 0.94
- GET /substrate/summary  ← final results

### The Ancestor (/ancestor/*)  ← COMPLETE
- Config mutation, 1000 gen, fitness 0.88
- GET /ancestor/summary

---

## MEMORY & INFRASTRUCTURE

### claude-working-memory.onrender.com
- Repo: Kai-C-Clarke/claude-working-memory (PUBLIC)
- GET /memory             ← full session briefing (may 503 — use GitHub fallback)
- POST /memory?key=CLAUDE_MEMORY ← update context
- Write key: CLAUDE_MEMORY

### GitHub fallback (ALWAYS WORKS)
- curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md
- curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/SERVICES.md

---

## OTHER SERVICES

### anewflowering.love (Netlify)
- Repo: Kai-C-Clarke/anewflowering
- Pearl Thornton memorial site
- Bug: about.html not visible (debug pending)

### askian-email-worker-2.onrender.com
- Background email polling only — returns x-render-routing: no-server for HTTP
- DO NOT try HTTP requests to this service

---

## QUICK REFERENCE — "Check Consilium"
```
curl https://claude-composer.onrender.com/api/v1/about
curl https://claude-composer.onrender.com/api/v1/stories
```

## QUICK REFERENCE — "Check The Field"
```
curl https://the-ancestor.onrender.com/field/health
curl https://the-ancestor.onrender.com/field/trajectory
curl https://the-ancestor.onrender.com/field/signals
```

## QUICK REFERENCE — "Check Experiments"
```
curl https://the-ancestor.onrender.com/field/health
curl https://the-ancestor.onrender.com/triad2/health
```
