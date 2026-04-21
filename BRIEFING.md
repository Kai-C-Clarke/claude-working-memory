# Jon Stiles — Session Context
Last updated: 21 April 2026 07:30 UTC

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

## THE FIELD — CURRENT STATE (21 Apr 2026)

**Running:** Cycle 5,520 | G=3,000 | Kills=185 | Signals=200 | Traj=39 | Locked=True

**This is a two-Claude collaboration.** This Claude (chat) handles debugging and infrastructure.
Project Claude (claude.ai/projects) handles architectural thinking and experimental design.
Project Claude identified the core flaw in v2 (telepathy) and drove the v3 rewrite.

### Architecture evolution

**v2 (original — "telepathy"):**
B watched A's mode field flip search→hunt, then read A's predicted_bloom position directly.
Not communication — direct state read. Partner_weight = sensitivity to a designed signal.
Result: zero signals for thousands of cycles.

**v3 (Project Claude's rewrite, 20 Apr — "spatial inference"):**
B removed from A's internal state entirely. B only observes A's position history (20-cycle window).
B measures A's recent vs previous displacement, detects acceleration >1.8× baseline.
If sustained acceleration detected, B extrapolates A's trajectory and moves toward inferred destination.
The only channel is spatial behaviour in a shared field.
Result: 200 signals at cycle 5,520. 185 kills. Architecture correct.

### Project Claude's subsequent refinements (20 Apr, 14 commits):

**1. Bloom-blind B (cba2f4d, 17:05)**
B's memory_len set to 0 — cannot accumulate bloom trajectory memory at all.
B must navigate entirely via inference from A's movement.
This makes B's survival genuinely dependent on reading A.
Fix: mem[-0:] bug (93e0f5fd) — memory_len=0 now truly prevents accumulation.

**2. Identity frequency + duty cycle (80b0e7e, 20:03)**
Each predator has a stable carrier frequency (id_freq) in band 1.4–1.8 Hz,
above all natural prey frequencies. Pulse duration (emit_duty) is a second identity dimension.
Together these constitute a persistent signature. Mode-switching modulates amplitude and speed,
NOT the base frequency. This lets B distinguish "A moving fast" from "random entity moving fast."
Exposed via id_freq and emit_duty in state endpoint.

**3. Directional consistency trigger (1174a3af, 16:54)**
Replaced acceleration-only trigger with directional consistency + straight-line detection.
B now looks for A moving in a consistent direction, not just moving fast.
More robust — eliminates false positives from random fast movement.

**4. Inference reinforcement (038642d2, 16:49)**
partner_obs_weight starts at 0.15 (not 0.0) — B begins with some observation sensitivity.
When B acts on inference AND that cycle produces a kill, obs_weight reinforced upward.
When B ignores inference, obs_weight decays. Selection pressure on observation behaviour.

**5. Ambush strategy for A (437ef5a9, 21:36)**
A positions at bloom EDGE (BLOOM_RADIUS × 2), not centre.
Problem: grazers have flee radius 0.35 rad — if A is at bloom centre,
grazers detect A and avoid the bloom entirely. No prey comes to A.
Solution: A waits outside flee detection zone. Grazers approach bloom to feed.
A ambushes from edge. This is a genuine behavioural strategy, not a parameter tweak.

**6. Fixes:**
- None-comparison TypeError on stale state (9ae9c3cd)
- Double distance decay bug (daee35ef)
- Teleport spike filter
- Signal threshold lowered to match observed speeds
- A action threshold lowered to 0.03 (kin-gated)

### What to watch:
- `/field/signals` — are signals correlating with subsequent kills?
- `obs_weight` — is B's observation sensitivity evolving upward?
- Does B's kill rate increase as obs_weight rises? (That would be selection for inference)
- Ambush strategy — do kills increase with A at bloom edge vs centre?

---

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
| Field experiments | the-ancestor.onrender.com | /field/health, /field/signals, /field/trajectory |
| Memory | claude-working-memory.onrender.com | /memory, /memory/autosave |
| Pearl | anewflowering.love | Memorial |

Deploy webhook: `https://api.render.com/deploy/srv-d6lk2v6a2pns73b2pf40?key=cY4Yuhb2q7Y`
Experiment write key: ancestor-2026
Consilium key: 3a51b60e9b78720f8528412db52e7ef3
GitHub PAT (Kai-C-Clarke): see Jon's password manager — expires Jun 2026 (expires Jun 2026)
SnapRender: sk_live_[REDACTED] (add to Render env as SNAPRENDER_API_KEY)

---

## OPEN THREADS

- **Field:** obs_weight not yet evolving — watch whether B's kills increase as inference matures
- **Field:** Ambush strategy just deployed — does kill rate improve?
- **Field:** First genuine signal→kill correlation would confirm the mammoth hypothesis
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
