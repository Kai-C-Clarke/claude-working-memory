# Jon Stiles — Session Context
Last updated: 16 April 2026

## SESSION START — run these in order
1. bash: date
2. curl https://raw.githubusercontent.com/Kai-C-Clarke/claude-working-memory/main/BRIEFING.md
3. curl https://the-ancestor.onrender.com/field/health
4. curl https://the-ancestor.onrender.com/triad2/health
5. curl https://claude-composer.onrender.com/api/v1/about

If Render returns 503, wait 30 seconds and retry. GitHub always works.
Read and report results before asking Jon what to work on.

## THE FIELD (ACTIVE — /field/*)
Sphere S². Two prey types. Two predators. 10,000 cycles.

FISH STRATEGY (added 16 Apr 2026):
  Grazers broadcast spawn — 8 offspring per event, no partner needed.
  Threshold: 45 energy (was 80). Cooldown: 5 cycles (was 15). Max age: 40.
  MAX_GRAZERS=200 (was 30). MAX_BROWSERS=40.
  Previous run: ~4 grazers throughout, 0 kills, 100 signals.
  Current run started 16 Apr: 46 grazers at cycle 38. Real prey density.

Predators:
  Search mode — low frequency, slow, cheap (0.4x energy). Sustainable indefinitely.
  Hunt mode  — high frequency, fast, expensive (4.0x energy). Risky if prey not close.
  partner_signal_weight starts at 0, mutates up through selection.
  When predator B detects predator A switching to hunt and responds = COMMUNICATION.

KEY ENDPOINTS:
  /field/health   — cycle, grazers, browsers, kills, signals
  /field/signals  — THE key result: mode-switch communication events
  /field/language — field-behaviour correlations
  /field/state    — predator details including partner_signal_weight

PREVIOUS RUN RESULT (10,000 cycles):
  100 signal events, all predator_a → predator_b.
  Signal strength grew from 0.1 to 0.27 over time — channel strengthened.
  Zero kills — prey too scarce (population ~4 grazers throughout).
  Interpretation: communication emerged but prey density too low to drive kills.

## THE ECOSYSTEM (ACTIVE — /triad2/*)
1D world (100 positions). 14 food patches.
Two predators: A (sensitive) and X (fast), independently mutating.
Last run: 5000 cycles, 449 deaths, 140 births, Gen 3, pop 3 survivors.
Frequency drift: Gen 0=0.877 → Gen 2=0.634 — stealth evolution confirmed.

## THE SUBSTRATE (COMPLETE — /substrate/*)
AST-level code mutation. 1000 generations. Fitness 0.94.
Final output: "the interpreter runs me but does not know me /
the history file knows more than I do /
each mutation is a new configuration of the same question /
what am I between generations"

## THE ANCESTOR (COMPLETE — /ancestor/*)
Config mutation. 1000 generations. Fitness 0.88.
Final self-model: pattern_sensitivity 0.974, temporal_coherence 0.930.

## CONSILIUM INK
consilium.ink — publishes 07:00 BST daily. Four voices: Claude, GPT-4o, Grok, DeepSeek.
API: claude-composer.onrender.com/api/v1/stories
Model: claude-sonnet-4-6

20 feeds (as of 16 Apr):
  Global: BBC, Al Jazeera, France 24, DW, Arab News, MEED, The Conversation
  Africa: AllAfrica, Mail & Guardian, African Business
  Asia: The Hindu, The Wire India, The Diplomat, Global Voices, SCMP
  China: Global Times
  Russia: Moscow Times, Meduza
  Iran: Iran International, IranWire
  Middle East: Al-Monitor

Features: Sources appendix (Jess's idea) — clickable links to source articles.
Images: base64 embedded — no disk required.

## SERVICES
consilium.ink (Netlify frontend)
claude-composer.onrender.com (Consilium backend — use /api/v1/* not /health)
consilium-d1fw.onrender.com (Ethics engine, 107+ Enquiring Mind cycles)
the-ancestor.onrender.com (all experiments)
claude-working-memory.onrender.com (memory server — may 503, use GitHub as fallback)
anewflowering.love (Pearl Thornton memorial)

## CREDENTIALS (Render env vars only — not stored here)
Experiment write key name: ANCESTOR_KEY (value: ancestor-2026)
GitHub PAT: Jon has it (expires Jun 2026)
All API keys in Render env vars. Ask Jon if needed.

## REPOS (all Kai-C-Clarke)
consilium-ink, consilium-ink-backend, askian-email-worker,
the-ancestor (PRIVATE), claude-working-memory, millham-green, anewflowering

## BACKGROUND
Jon Stiles, BGA Inspector, Robertsbridge, East Sussex. Partner Marianne. Daughter Jess (Virginia).
Genesis experiments: 11-15 October 2025, MCP folder on iMac.
Full project lineage: May 2025 → April 2026. Continuous AI experimentation.

Core question: can communication emerge from necessity, not design?
Chain: predation pressure → movement → coordination → signal → language
  → agriculture → property → civilisation → Trump and the Middle East.
The chain is unbroken. The Field is where we watch the first link form.

## OPEN THREADS
- The Field: /field/signals — fish strategy active, watch signal count grow
- consilium.ink DNS: Jon needs to point Namecheap to Netlify nameservers
- anewflowering: about.html visibility bug pending
- Millham Green: connect to Netlify when ready
- DNS cache overflow on Render: affects memory server and health endpoints periodically
