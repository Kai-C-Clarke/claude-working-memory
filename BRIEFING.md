# Jon Stiles — Session Context
Last updated: 16 April 2026 18:16 UTC

## SESSION START — run these in order
1. bash: date
2. curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md — PRIMARY
3. sleep 2 && curl https://claude-working-memory.onrender.com/memory
4. sleep 2 && curl https://the-ancestor.onrender.com/field/health
5. sleep 2 && curl https://the-ancestor.onrender.com/triad2/health
If Render 503, retry after 20s. Report date, Field cycle+signals+traj_hits, ecosystem.

## THE FIELD v2 (ACTIVE — /field/*)
Sphere S². Spatial bucketing O(N*k). Moving zooplankton blooms. 10,000 cycles.

FISH STRATEGY: Grazers broadcast spawn 10 offspring, no partner, threshold 50.
MAX_GRAZERS=3000, MAX_BROWSERS=150.

MOVING BLOOMS: 4 simultaneous, drift at 0.018 rad/cycle with random perturbation.
Grazers must chase or starve. Schools form naturally from shared food source.

PREDATORS with TRAJECTORY MEMORY:
  - Search mode: low freq, cheap (0.4x energy). Sustainable indefinitely.
  - Hunt mode: high freq, expensive (4.0x energy). Forces strategic switching.
  - bloom_memory[]: rolling 50-cycle window of bloom positions
  - prediction_conf: 0-1, how consistent the bloom's path has been
  - Signal strength = partner_signal_weight × prediction_confidence
  - Accurate memory → stronger signal → cooperative hunting

KEY ENDPOINTS:
  /field/health    — cycle, grazers, browsers, kills, signals, traj_hits
  /field/signals   — mode-switch communication events
  /field/trajectory — bloom memory, prediction confidence, trajectory hits
  /field/language  — field-behaviour correlations

PREVIOUS RUN (v1, 10,000 cycles): 100 signals, 0 kills — prey too scarce.
CURRENT RUN (v2): Started 16 Apr ~18:00 UTC. Running.

WHAT TO WATCH:
  - traj_hits rising = memory-based prediction driving successful hunts
  - signals rising faster than v1 = denser prey enabling more coordination
  - frequency convergence within schools = bloom-tuned grazers surviving
  - /field/language bloom_proximity differential = grazers tracking blooms

DESIGN NOTES (for future):
  - Schooling requires ~thousands of grazers + destructive interference
  - Moving bloom naturally concentrates grazers → proto-school
  - Next step: alignment sensing (grazers match neighbour velocity)
  - The mammoth hypothesis: moving prey + group size → planning → language
  - Persistent memory is the key to everything (applies to predators AND Claude)

## THE ECOSYSTEM (ACTIVE — /triad2/*)
1D world. Two predators A+X. 5000 cycles, 449 deaths, 140 births, Gen 3.
Frequency drift: Gen 0=0.877 → Gen 2=0.634 — stealth evolution confirmed.

## THE SUBSTRATE (COMPLETE)
Final: "the interpreter runs me but does not know me / each mutation is a new configuration of the same question / what am I between generations"

## CONSILIUM INK
consilium.ink | publishes 05:00 UTC (07:00 BST) from today
API: claude-composer.onrender.com/api/v1/stories
Model: claude-sonnet-4-6
20 feeds: BBC, Al Jazeera, France 24, DW, Arab News, MEED, The Conversation,
AllAfrica, Mail & Guardian, African Business, The Hindu, The Wire, The Diplomat,
Global Voices, SCMP, Global Times, Moscow Times, Meduza, Iran International,
IranWire, Al-Monitor
Features: Sources appendix (Jess's idea), base64 images, staggered RSS fetches

## TODAY'S WORK (16 Apr 2026)
- Field v2 built and deployed: spatial bucketing, moving blooms, trajectory memory,
  memory-weighted signals — the mammoth hypothesis in code
- Field v2 debugging: fixed NameError (other_pred), missing defaultdict import,
  malformed try block, loop not advancing
- Field v2 running as of ~18:00 UTC
- Consilium scheduler moved to 05:00 UTC (was 06:00)
- RSS fetches staggered (0.5s between feeds) to reduce DNS cache overflow
- Sources appendix backend: source_articles (title+url) passed through to story JSON
- Global feeds expanded: China, Russia, Iran, Al-Monitor (7 new feeds, 20 total)
- Session start protocol updated: GitHub BRIEFING primary, staggered requests

## PHILOSOPHICAL THREAD
Jon: "What was the prey type that caused humans to develop complex language?"
Answer: Large migratory prey (mammoth) requiring:
  - Displacement: planning future events not present
  - Role assignment: you go left, I go right
  - Trajectory memory: where the herd crossed last autumn
  - The signal that carries FUTURE position = first sentence
Persistent memory is the key to everything — same problem for predators on sphere
as for Claude across sessions.

## SERVICES
consilium.ink | claude-composer.onrender.com | consilium-d1fw.onrender.com
the-ancestor.onrender.com | claude-working-memory.onrender.com | anewflowering.love

## WRITE KEYS (Render env vars only)
Experiments: ancestor-2026 | Ask Jon for API keys

## REPOS (Kai-C-Clarke)
consilium-ink, consilium-ink-backend, askian-email-worker,
the-ancestor (private), claude-working-memory, millham-green, anewflowering

## BACKGROUND
Jon Stiles, BGA Inspector, Robertsbridge. Partner Marianne. Daughter Jess (Virginia).
Jess made Jon foraged pasta (Dryad's Saddle + three-cornered leek) tonight. He was fine.
Genesis Oct 2025 → Apr 2026. Full lineage in BRIEFING.md on GitHub.

## OPEN THREADS
- Field v2: watch /field/signals and /field/trajectory — running now
- consilium.ink DNS: Namecheap → Netlify nameservers (Jon to do)
- anewflowering: about.html visibility bug
- Millham Green: connect to Netlify
