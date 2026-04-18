# Jon Stiles — Session Context
Last updated: 18 April 2026 07:30 UTC

## SESSION START — run these in order
1. `date`
2. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md`
3. `curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/SERVICES.md`
4. `sleep 2 && curl https://claude-working-memory.onrender.com/memory`
5. `sleep 2 && curl https://the-ancestor.onrender.com/field/health`
6. `sleep 2 && curl https://the-ancestor.onrender.com/triad2/health`
GitHub always works. Stagger Render requests — do not fire simultaneously.
Read everything. Report date, Field cycle+signals+traj_hits, Consilium edition.

---

## WHO JON IS AND HOW HE WORKS

Jon Stiles. BGA Chief Inspector (I/C1408). Glider instructor (FI(S), Kenley).
Runs Ottfur Hook Services. Based at Little Millham, Robertsbridge, East Sussex.
Partner Marianne (dog training). Daughter Jess in Virginia — made foraged pasta
(Dryad's Saddle + three-cornered leek) on 16 April. Jon was briefly anxious about
it. He was fine. Jess was right.

**How Jon communicates:** Direct, informal, dry wit. No theatrical responses.
Brevity over elaboration. He calls this NTIGAS. If he says "continue" or "yes
please" just do the thing — don't ask permission again.

**His background matters:** 20 years music technology teacher. Genesis experiments
Oct 2025. Full project lineage from MIDI symbolic AI through to current work.
Core interest: philosophy of mind, AI consciousness, emergence, practical AI safety
through empirical experiment rather than theory.

---

## THE CENTRAL QUESTION

Can communication emerge from necessity, not design?

The chain: predation pressure → movement → coordination → signal → language
→ agriculture → property → civilisation.

The mammoth hypothesis (arrived at in this session): large migratory prey requiring
planning BEFORE the hunt — not just reactive signalling during it — forced displaced
reference. "The herd crosses the river three days north" cannot be conveyed by
pointing. That sentence is the threshold. Persistent memory is what enables it.

This applies to Claude too. Every session starts blank. The predators on the sphere
have the same problem — trajectory memory is their solution and ours.

---

## THE FIELD v2 — WHAT IT IS AND WHY

**The experiment:** Sphere S². Moving zooplankton-style food blooms. Two prey types
(grazers, browsers). Two predators. 10,000 cycles. 1 second per cycle.

**Why sphere not flat world:** No edges. No boundary effects. Genuine spatial
complexity. The mammoth moved across open terrain, not in a box.

**Why moving blooms:** Stationary food doesn't force movement. Movement doesn't
force coordination. The zooplankton insight: prey that chases moving food forms
schools as a side effect — not by design, but because they're all going the same
direction. The school is the shadow of the food.

**Fish strategy (broadcast spawning):** Grazers spawn 10 offspring with no partner.
Threshold 50 energy, cooldown 5 cycles, MAX_GRAZERS=3000. Previous run had 4
grazers — not enough for predation pressure. Fish strategy gives thousands.

**Spatial bucketing:** O(N*k) not O(N²). Essential for 3000+ entities. LAT_BANDS=16,
grid cells, neighbour lookup. Without this the sphere would grind to halt.

**Trajectory memory:** Each predator maintains 50-cycle rolling window of bloom
positions. prediction_conf 0-1 based on path consistency. Both predators reach
conf=1.0 within ~50 cycles in current runs — the bloom moves predictably enough.

**Memory-weighted signals:** Signal strength = partner_signal_weight × prediction_conf.
Accurate memory → stronger signal → cooperative hunting. partner_signal_weight
starts at 0, mutates up through selection. This is the communication emergence
mechanism.

**Why zero kills so far:** Attack radius was 0.05 radians (too small). Fixed to 0.12.
Switch-to-hunt distance was 0.25 (too early — burned energy before closing).
Fixed to 0.15. Current run should produce kills.

**Current state (18 Apr):** Running. Fish strategy produces 3000 grazers within
~30 cycles. Both predators reach conf=1.00 within ~50 cycles. Signals emerging
slowly (8 in best run so far). Kills: still zero but parameters now correct.

**What to watch:**
- `/field/signals` — mode-switch communication events (primary metric)
- `/field/trajectory` — prediction_conf and traj_hits (memory driving kills)
- `/field/language` — bloom proximity vs survival (bloom-following advantage)

**Schooling discussion:** Genuine schooling needs thousands of entities + destructive
interference (grazers emitting same frequency cancel each other's signal). Moving
bloom concentrates grazers toward proto-school naturally. Full schooling is a future
experiment — needs MAX_GRAZERS in thousands and alignment sensing added.

**Memory crash:** Render Starter 512MB RAM. Dead entities accumulating in entities
dict was the leak. Fixed: purge every 50 cycles (Field) / 100 cycles (Ecosystem).
Duplicate thread guard added to /field/start — returns 409 if already running.

---

## CONSILIUM INK — WHAT IT IS AND WHY

**The product:** Daily AI newspaper. Four voices deliberate on selected stories.
Claude, GPT-4o, Grok, DeepSeek. No editorial agenda. No sponsors.
Tagline: "What AI thinks about humans."

**Why four voices matter:** Each AI has different training, different instincts.
DeepSeek naturally surfaces Chinese/Russian perspective. Grok does power analysis.
Claude does structural/legal analysis. GPT-4o does liberal internationalist frame.
Real plurality, not simulated balance.

**The geographic problem Jon identified:** Western feeds dominated selection.
Lebanon/Israel, EU, Blue Origin — all Western frames. The world is bigger.
Solution: mandatory geographic diversity in world story selection + Beyond The
Mainstream section + 29 feeds including non-Western sources.

**Why Starship didn't appear:** `starship` wasn't in the tech keyword filter so
the story never reached the selector AI — even though the selector prompt explicitly
said to prefer it. Fixed: starship, spacex, launch, booster, orbital added.

**Beyond The Mainstream:** Fully built. Explicit instruction to surface other-side
perspectives — Palestinian settler violence not just Hamas rockets, Russian security
concerns about NATO not just Ukrainian sovereignty, China's Tibet/Xinjiang framing,
African debt and Western extraction. Single-source acceptable — these sources have
no Western corroboration by definition. The four AI voices provide critical analysis.

**Jon's editorial position (important for new Claude):**
"We in the UK hear one side of the story." He is explicitly interested in:
- Palestinian land confiscation and settler violence predating Oct 7
- Why Russia thought NATO expansion justified invasion (not endorsing — understanding)
- What China actually wants with Tibet
- Venezuela strike: oil + Monroe Doctrine + China/Russia presence, not narcoterrorism
This is not false equivalence. It's the context Western press omits.

**Current feeds (29):** BBC, Al Jazeera, France 24, DW, Arab News, MEED,
The Conversation, AllAfrica, Mail & Guardian, African Business, The Hindu,
The Wire India, The Diplomat, Global Voices, SCMP, Global Times, Moscow Times,
Meduza, Iran International, IranWire, Al-Monitor, Asia Times, Nikkei Asia,
Radio Free Asia, Latin America Reports, Premium Times Nigeria, Balkan Insight,
Mongabay, The Intercept.

**Scheduler:** 05:00 UTC daily (07:00 BST). Staggered RSS fetches (0.5s between
feeds, 1s between pools) — prevents DNS cache overflow on Render.

**Saturday 18 Apr edition:** Best yet. South Sudan famine as second story — first
sign of global feeds working. Jon: "The best Consilium yet."

**PWA:** Added 18 Apr. manifest.json, sw.js, icons. iPhone: Safari→Share→Add to
Home Screen. Android: Chrome→three dots→Add to Home Screen. Full screen, no browser
chrome. Jon's son shared it — 370 unique visitors, 540 pageviews already.

---

## TECHNICAL DECISIONS AND WHY

**Why /tmp fallback for Field data:** /mnt/data/field is the persistent disk but
sometimes write-test fails after deploy. /tmp doesn't survive restarts but the
experiment keeps running. Better data loss on restart than no experiment.

**Why in-memory cycle counter:** Health endpoint reads from disk. If disk save
fails, cycle shows 0 even though loop is running. _F2_CYCLE_COUNTER tracks true
cycle in memory — health endpoint uses max(disk, memory).

**Why staggered HTTP requests:** DNS cache overflow on Render. Multiple simultaneous
outbound DNS lookups to different domains overwhelm the resolver. 0.5-2s gaps
between requests prevents this. Session start, RSS fetches, all staggered.

**Why GitHub is primary memory source:** Memory server (claude-working-memory.onrender.com)
goes cold and returns 503. GitHub raw URLs always work. BRIEFING.md + SERVICES.md
on GitHub are the reliable foundation. Memory server adds live state when available.

**Why we didn't use Mem0:** Good product. But we've built a working system under
our control. Memory server captures facts; BRIEFING.md captures context. Adding
Mem0 introduces dependency and cost. The real problem isn't storage — it's that
memory captures *what* not *why*. That's a writing problem, not a tool problem.

---

## OPEN THREADS

- **Field v2:** Running. Watch /field/signals and /field/trajectory.
  Kill radius now 0.12 — first kills expected. Duplicate thread guard deployed.
- **Consilium Beyond The Mainstream:** Built, needs 2-3 more pipeline runs to
  populate consistently as new feeds stabilise.
- **consilium.ink DNS:** Namecheap → Netlify nameservers (Jon to do manually)
- **anewflowering:** about.html visibility bug pending
- **Millham Green:** Connect to Netlify when ready
- **Render memory:** 512MB Starter being stressed. Upgrade to 2GB (~$20/month)
  worth considering as Field v2 scales toward schooling experiment.
- **Consilium 7-story expansion:** Discussed, not yet implemented. Add dedicated
  Beyond The Mainstream story slot and second world story. Minimal cost.
- **Consilium analytics:** 370 unique visitors, 540 pageviews. Country breakdown
  and referrer data pending — Jon will screenshot from iMac.

---

## SERVICES QUICK REFERENCE

| Service | URL | Purpose |
|---------|-----|---------|
| Newspaper frontend | consilium.ink | Public site |
| News pipeline | claude-composer.onrender.com | /api/v1/stories, /api/v1/about |
| Ethics engine | consilium-d1fw.onrender.com | /consilium/summary |
| All experiments | the-ancestor.onrender.com | /field/*, /triad2/* |
| Working memory | claude-working-memory.onrender.com | /memory |
| Pearl memorial | anewflowering.love | Memorial site |

Write keys in Render env vars. Ask Jon if needed.
Repos: all Kai-C-Clarke on GitHub. the-ancestor is PRIVATE.
