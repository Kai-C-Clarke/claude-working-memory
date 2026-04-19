# Jon Stiles — Session Context
Last updated: 19 April 2026 21:20 UTC

## SESSION START — run these in order
1. `date`
2. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md`
3. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/SERVICES.md`
4. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/THOUGHT_MAP.md`
5. `sleep 2 && curl https://claude-working-memory.onrender.com/memory`
6. `sleep 2 && curl https://the-ancestor.onrender.com/field/health`
7. `sleep 2 && curl https://the-ancestor.onrender.com/triad2/health`
GitHub always works. Stagger Render requests. Read everything before asking what to work on.

---

## HOW TO UPDATE THIS BRIEFING
Write like a colleague handing over to another colleague — not like release notes.
Capture WHY decisions were made, not just what was done.
The facts are in the code. The reasoning is only here.

---

## WHO JON IS AND HOW HE WORKS

Jon Stiles. BGA Chief Inspector (I/C1408). Glider instructor (FI(S), Kenley).
Runs Ottfur Hook Services. Based at Little Millham, Robertsbridge, East Sussex.
Partner Marianne (dog training). Daughter Jess in Virginia.

Communication: Direct, informal, dry wit. NTIGAS principle — no theatrical responses.
When Jon says "continue" or "yes please" — just do it, don't ask again.
When Jon says "save please and write it all up" — write a comprehensive BRIEFING update.

Engineering instinct: identifies root cause precisely, prefers minimal fix, keeps backups.
Applies BGA Inspector risk assessment logic to code — what is actually failing, not what appears to be.

Previous work: K_Spk consciousness transfer (Aug 2025), LLM Café, Genesis Project,
Remote Operator UI automation, PIE, Claude_Local with 3D spatial memory.
The ideas were always right. The tooling needed time to catch up.

---

## THE CENTRAL QUESTION
Can communication emerge from necessity, not design?
Chain: predation pressure → movement → coordination → signal → language → agriculture → civilisation.

The mammoth hypothesis: large migratory prey requiring planning BEFORE the hunt forced
displaced reference. "The herd crosses the river three days north" cannot be pointed to.
That sentence = displaced reference = the threshold. Persistent memory enables it.
Same problem for predators on the sphere as for Claude across sessions.

---

## THE FIELD v2 — CURRENT STATE (19 Apr 2026)

**Running.** Cycle 23, 3,000 grazers, locked, stable.
Both predators: conf=1.000, memory=23, partner_weight=0.000

**Architecture:**
- Sphere S². Spatial bucketing O(N*k). Moving zooplankton blooms (BLOOM_SPEED=0.018).
- Fish strategy: broadcast spawn 10 offspring, threshold 40, MAX_GRAZERS=3000.
- Predators: trajectory memory 50 cycles, prediction_conf 0-1, memory-weighted signals.
- Kill radius: 0.12 (was 0.05 — too small). Switch dist: 0.15 (was 0.25 — too early).
- Bloom energy: 80 × 0.4 multiplier = 32/cycle max (was 40 × 0.15 = 6/cycle — grazers starving).

**Bugs fixed this session (19 Apr):**
- KeyError: 'damage' — not in predator dict after JSON reload. Fixed: added to new_predator().
- Tuple/list JSON deserialisation: bloom_memory positions become lists after reload. Fixed with tuple().
- Dead entities accumulating: purge every 50 cycles. Fixed memory leak.
- Duplicate thread: persistent lock file .field_running on disk. Fixed.
- Bloom memory cleared on starvation reset: now preserved, predator respawns near predicted bloom.
- Food delivery: 0.15 multiplier meant grazers starved even on bloom. Fixed to 0.4.

**Why zero kills still:** partner_weight starts at 0.000, needs to mutate up through selection.
Memory entries at 23/50 — still building. No resets happening now. Give it overnight.

**What to watch:** /field/signals (mode-switch communication), /field/trajectory (traj_hits).
The first kill followed by a signal event = the mammoth hypothesis beginning to work.

---

## CONSILIUM INK — CURRENT STATE (19 Apr 2026)

**Published:** consilium.ink | 05:00 UTC daily (07:00 BST)
**Backend:** claude-composer.onrender.com
**Model:** claude-sonnet-4-6 (DeepSeek primary writer, Claude/GPT-4o/Grok voices)

**32 feeds** including: BBC, Al Jazeera, France 24, DW, AllAfrica, Mail & Guardian,
African Business, The Hindu, The Wire India, The Diplomat, Global Voices, MEED, SCMP,
Global Times, Moscow Times, Meduza, Iran International, IranWire, Al-Monitor,
Asia Times, Nikkei Asia, Radio Free Asia, Latin America Reports, Premium Times Nigeria,
Balkan Insight, Mongabay, The Intercept, Financial Times, Google News, Forbes via Google.

**Editorial pipeline (as of 19 Apr):**
1. Gather RSS from 32 feeds (staggered 0.5s)
2. EDITORIAL MEETING (new): enrich top 25 articles with full text, four voices deliberate,
   each nominates 3 stories with editorial reasoning, DeepSeek synthesises final brief
3. Select stories (DeepSeek selector)
4. Write articles (DeepSeek writer)
5. Four voice deliberation (each voice uses own model)
6. Editorial data check: catches voice refusals, regenerates bad quotes automatically
7. VISUAL QA (new): SnapRender screenshots consilium.ink → Claude vision editorial review
8. Save edition

**New features added 19 Apr:**
- Share buttons: Web Share API (native Android/iOS share sheet) + WhatsApp/X/LinkedIn
- Single-story layout: full-width with image right or centred, no empty column
- Beyond The Mainstream: live, non-western sources in pool
- Claude voice refusal fix: removed jailbreak-triggering "CRITICAL BRIEFING PROTOCOL"
- /news/patch endpoint: fix individual voice quotes without regenerating edition
- Editorial meeting: /api/v1/meeting endpoint with transcript
- Visual QA: /api/v1/visual-qa endpoint with Claude vision report
- SnapRender key: sk_live_Slk66JG7__3-wo6QWOtPRewdWo4EI-5h (added to Render env vars)
  SNAPRENDER_API_KEY must be set in consilium-ink-backend on Render

**Analytics (19 Apr):** 540 pageviews, 370 unique visitors in first week.
Countries: USA 224, China 76, Singapore 40, UK 38, Canada 23, Germany 15, Japan 15.
China at 76 is remarkable for a new publication with no promotion.

**The Claude refusal problem (19 Apr):**
Claude voice called the Hormuz story "fabricated" — because the prompt contained
"Do NOT refuse to engage" which Claude's safety training reads as a jailbreak attempt.
Fixed: prompt now cites actual sources directly ("BBC World: Strait of Hormuz closed again").
Lesson: never tell Claude what NOT to do. Tell it what you have and ask it to analyse.

**Editorial philosophy Jon established:**
"We in the UK hear one side of the story." Consilium should surface:
- Palestinian settler violence not just Hamas rockets
- Russian security concerns about NATO not just Ukrainian sovereignty  
- China's Tibet/Xinjiang framing not just Western human rights narrative
- Venezuela = oil + Monroe Doctrine + China/Russia presence, not narcoterrorism
Not false equivalence. The context Western press omits.

---

## THE EDITORIAL MEETING (NEW — first run tonight)

Four voices with fixed positions deliberate on full story pool before writing:
- Claude: structural analyst — institutional logic, cui bono, precedent
- DeepSeek: Global South — surfaces non-Western stories, challenges Western framing
- Grok: contrarian — what's everyone missing, what's being framed wrong
- GPT-4o: liberal internationalist — human rights, rule of law, accountability

Each reads full article text (not just RSS summaries), nominates top 3 with reasoning.
DeepSeek synthesises into final brief (10x cheaper than Claude for logic tasks).
Transcript published at /api/v1/meeting — transparent editorial judgment.

First pipeline run with meeting: triggered 19 Apr ~21:20 UTC. Results tomorrow.

---

## VISUAL QA (NEW — first run tonight)

After each pipeline:
1. SnapRender screenshots consilium.ink (1440×900 PNG)
2. Sent to Claude vision with editorial brief
3. Report checks: layout balance, share button visible, headlines readable, nav correct
4. Saved at /api/v1/visual-qa
5. Uses 1 of 500 free monthly screenshots

This automates what Jon was doing manually by looking at the published page.

---

## WORKSHOP & MACMINI PLANS

Workshop at Little Millham: screed going in next week. Floor sealed with green PVA.
Cable runs above roof trusses — complete flexibility, no conduit in screed needed.
Power: modern consumer unit, fed from house. UPS needed (~£100-150 for 1000VA).
Network: Cat6 from house via trusses. PoE cameras × 3 (wide-angle, bench-mount, entrance).
MacMini: M5/M5 Pro expected WWDC June 8. 500 free screenshots/month SnapRender.

**The MacMini memory system (future):**
- Local vector store (Chroma/LanceDB) + embedding model (Ollama)
- Continuous association engine — keyword + image + feeling anchors
- MCP server exposes: search_memory(), get_strand(), get_context()
- Claude queries live graph throughout conversation, not just at session start
- Workshop camera feed + vision model = spatial awareness (tool location, FOD detection)
- The Circle (family memory app) + Claude memory system = same architecture, different data

Jon's memory model: keyword + image + feeling → retrieves vast context from small anchor.
Current BRIEFING is the hand-built version of this. MacMini system will automate it.

---

## COST OPTIMISATION

Monthly costs (approximate):
- Render (ancestor + consilium + memory): ~£21/month
- DeepSeek (bulk writing, selection, synthesis): ~£3-5/month
- Claude (voice + visual QA): ~£8-12/month
- GPT-4o (voice): ~£5-8/month
- Grok (voice): ~£3-5/month
- SnapRender (visual QA): free (500/month)
- Namecheap (consilium.ink): ~£25/year
Total: ~£40-51/month

DeepSeek handles: article writing, story selection, editorial synthesis, structural checks.
Each voice uses own model for: nominations and published quotes (genuine difference needed).
Claude handles: vision QA, complex structural analysis.

---

## SERVICES QUICK REFERENCE

| Service | URL | Key endpoints |
|---------|-----|---------------|
| Newspaper | consilium.ink | Public |
| News pipeline | claude-composer.onrender.com | /api/v1/stories, /api/v1/meeting, /api/v1/visual-qa, /news/patch |
| Ethics engine | consilium-d1fw.onrender.com | /consilium/summary |
| Experiments | the-ancestor.onrender.com | /field/health, /field/signals, /field/trajectory |
| Memory | claude-working-memory.onrender.com | /memory, /memory/autosave |
| Pearl | anewflowering.love | Memorial |

Write keys in Render env vars. the-ancestor repo is PRIVATE.
Experiment write key: ancestor-2026

---

## OPEN THREADS

- **Field v2:** Running, cycle 23. Watch /field/signals for first kill + signal event.
  partner_weight needs overnight to mutate up from 0.
- **Consilium editorial meeting:** First run triggered tonight. Check /api/v1/meeting tomorrow.
- **Consilium visual QA:** First run triggered tonight. Check /api/v1/visual-qa tomorrow.
- **consilium.ink DNS:** Still needs Namecheap → Netlify nameservers (Jon to do manually).
- **anewflowering:** about.html visibility bug pending.
- **Millham Green:** Connect to Netlify when ready.
- **MacMini:** Wait for WWDC June 8. M5 Pro target. Then build memory system.
- **SnapRender future use:** Screenshot news sources for full-page extraction.
  Replaces the three-virtual-display coordinate-based system from 2025.
