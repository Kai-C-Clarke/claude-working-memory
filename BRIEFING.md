# Jon Stiles — Session Context
Last updated: 25 April 2026 08:30 UTC

## SESSION START — run these in order
1. `date`
2. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md`
3. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/SERVICES.md`
4. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/THOUGHT_MAP.md`
5. `sleep 2 && curl https://the-ancestor.onrender.com/field/health`
6. `sleep 2 && curl https://claude-composer.onrender.com/api/v1/about`
GitHub always works. Stagger Render requests. Read everything before asking what to work on.

---

## WHO JON IS AND HOW HE WORKS
BGA Chief Inspector I/C1408, Robertsbridge, East Sussex. Partner Marianne. Daughter Jess (Virginia).
Communication: direct, informal, dry wit. NTIGAS — no theatrical responses.
When Jon says "continue" or "yes please" — just do it, no questions.
When Jon says "save please and write it all up" — write a full BRIEFING and push to GitHub.
Apply BGA Inspector logic to code: identify root cause precisely, minimal fix.

---

## THE CENTRAL QUESTION
Can communication emerge from necessity, not design?
Chain: predation pressure → movement → coordination → signal → language.
The mammoth hypothesis: large migratory prey requiring planning BEFORE the hunt
forced displaced reference — "the herd crosses the river three days north."
That sentence cannot be pointed to. It is the threshold.
Persistent memory enables it. Same problem for predators on the sphere as for Claude across sessions.

---

## THE FIELD — CURRENT STATE (25 Apr 2026)

**Running:** the-ancestor.onrender.com | service: origin-experiment-v2
**Endpoints:** /field/health | /field/bm | /field/summary | /field/hunters

### The experiment question
"Does entity A modify the behaviour of entity B, and by what means?"

### Architecture — v2 (complete rewrite, 23-24 Apr 2026)
All previous versions (spatial inference, telepathy, obs_weight) have been RETIRED.
The current experiment starts from first principles.

**Core rules:**
- No move_toward() — ever
- No hunt radius — feeding is contact only (radius 1.2 grid cells)
- Energy is conserved throughout (pool starts at 200,000)
- Nothing is given that physics would not give

**The stack (bottom up):**
1. Planetary field — 8 hotspots drifting slowly across 60×60 grid
2. Blooms — form at hotspots, emit radial fields, leave residue on death (marine snow)
3. Grazers — pure Brownian motion + chemokinesis (field boosts agitation, not direction)
4. Hunters — same Brownian motion, emit field modulated by energy state (metabolism leaking into field)

**Key insight:** Hunter emission is modulated by proximity to prey — a well-fed hunter
emits differently from a hungry one. Nobody designed this as a signal.
It is simply metabolism leaking into the field.

**Somatic mutation:** Every entity has 0.0002 probability per cycle of random genome change.
Mostly harmful. Occasionally produces novelty.

**BM measurement:** Compares hunters receiving strong field signals vs hunters not receiving signals.
Did the signal group move closer to grazers than the no-signal group?
Positive = yes. Sustained positive trend = something is happening.

### Current status (25 Apr morning)
- Cycle ~228,000 | Generation ~2,249
- 1.03 billion signals processed
- bm_recent: 0.0 (sparse measurement — needs both signal AND food proximity simultaneously)
- bm_trend: 0.0 (flat)
- Ecosystem stable: ~300 hunters, ~140 grazers, ~10 blooms

### What to watch
- bm_recent spikes (saw +1.27 at cycle 9,700-9,900 before settling)
- Whether positive spikes strengthen over generations
- bm_trend turning consistently positive

### Technical note
Service runs as: python ancestor.py (NOT gunicorn — gunicorn starved the simulation thread)
Start command set directly in Render dashboard, not via render.yaml.
Render ignores render.yaml startCommand and auto-detects Python → gunicorn.

## CONSILIUM INK — CURRENT STATE (21 Apr 2026)

**Live:** consilium.ink | Edition 28 | 05:00 UTC daily
**Backend:** claude-composer.onrender.com (app.py + editorial_meeting.py)

### Pipeline (in order):
1. Gather 32 RSS feeds (staggered)
2. Editorial meeting: enrich top 25 articles with full text, four voices deliberate,
   each nominates 3 stories, DeepSeek synthesises final brief
3. Select stories
4. Write articles (DeepSeek)
5. Four voice deliberation (each voice uses own model)
6. Editorial check: catches refusals, regenerates bad quotes
7. Visual QA: SnapRender screenshot → Claude vision editorial review
8. Save edition

### Editorial positions (fixed):
- Claude: structural analyst — institutional logic, cui bono, precedent
- DeepSeek: Global South — surfaces non-Western stories, challenges Western framing
- Grok: contrarian — what's everyone missing, what's being framed wrong
- GPT-4o: liberal internationalist — human rights, rule of law, accountability

### Fixes made 20-21 Apr:
- **Editorial guard threshold:** Was 600 chars — too tight, stripping legitimate Claude/Grok
  analyses (typically 450-600 chars). Raised to 1200, rely on phrase detection not length.
  Root cause: designed to catch refusals but caught good analysis instead.
- **Science writing prompt:** Reversed previous "do not summarise for lay audience" instruction.
  Now explicitly requires plain-language deck and "Why this matters" closing line.
  Bad: "Astrocyte-mediated calcium signalling creates dual-timescale memory"
  Good: "Brain support cells may be the key to how we form memories"
- **Share button:** Moved to nav bar (same black bar as Front Page, Geopolitics etc).
  Previous location (masthead-rule) was invisible on Android — dark background.
  Nav bar is guaranteed visible on all devices. Sits right of About tab.
- **Enquiring Mind truncation:** white-space:nowrap → normal, 2-line clamp.
  Visual QA caught this on first run — "looks unfinished and unprofessional."

### Visual QA first report (20 Apr 05:06, Edition 27):
"Generally balanced. Three-column lower grid works well."
FLAG: Enquiring Mind question truncated. FLAG: article ellipsis mid-word.
Share button ✅ visible. All nav tabs ✅. Verdict: Publishable with minor fixes.
Both flags actioned immediately.

### Analytics (19 Apr): 540 pageviews, 370 unique visitors week 1.
USA 224, China 76, Singapore 40, UK 38, Canada 23, Germany 15, Japan 15.
China at 76 remarkable for week 1 with no promotion.

### Cost structure:
- DeepSeek (bulk): ~£3-5/month
- Claude (voice + visual QA): ~£8-12/month
- GPT-4o (voice): ~£5-8/month
- Grok (voice): ~£3-5/month
- SnapRender: free (500/month, using ~30)
- Total: ~£19-30/month

---

## SERVICES QUICK REFERENCE

| Service | URL | Notes |
|---------|-----|-------|
| Newspaper | consilium.ink | Netlify |
| News backend | claude-composer.onrender.com | /news/state, /news/patch, /api/v1/meeting, /api/v1/visual-qa |
| Ethics engine | consilium-d1fw.onrender.com | /consilium/summary |
| Field experiments | the-ancestor.onrender.com | /field/health, /field/bm, /field/summary, /field/hunters |
| Memory | claude-working-memory.onrender.com | /memory, /memory/autosave |
| Pearl | anewflowering.love | Memorial |

Deploy webhook: `https://api.render.com/deploy/srv-d6lk2v6a2pns73b2pf40?key=cY4Yuhb2q7Y`
Experiment write key: ancestor-2026
Consilium key: 3a51b60e9b78720f8528412db52e7ef3
GitHub PAT (Kai-C-Clarke): see Jon's password manager — expires Jun 2026 (expires Jun 2026)
SnapRender: sk_live_[REDACTED] (add to Render env as SNAPRENDER_API_KEY)

---

## OPEN THREADS

- **Field v2:** bm oscillating around zero — watch for sustained positive trend over generations
- **Field v2:** Update field.html on consilium.ink with v2 description and live bm chart
- **Field v2:** Consider arms race mechanic — blooms evolving emission suppression
- **Consilium:** Share button on Android — now in nav bar, confirm visible
- **Consilium:** Article share buttons in modal — check renderShare working
- **consilium.ink DNS:** Namecheap → Netlify nameservers (Jon to do)
- **anewflowering:** about.html visibility bug pending
- **Millham Green:** Connect to Netlify when ready
- **MacMini:** WWDC June 8. M5 Pro target. Then proper memory system with vector store.
- **GitHub PAT:** Expires June 2026 — rotate before MacMini setup

---

## TWO-CLAUDE WORKING MODEL
Project Claude (claude.ai/projects): architectural thinking, experiment design, long-form reasoning.
This Claude (chat): debugging, infrastructure, deployment, rapid fixes.
Both read BRIEFING.md on session start. Commits by Project Claude pushed via Jon.
The collaboration is itself an experiment in AI coordination — two instances, shared memory via GitHub.
