# Jon Stiles — Session Context
Last updated: 15 April 2026

## SESSION START — run these in order
1. bash: date
2. curl https://claude-working-memory.onrender.com/memory
3. curl https://the-ancestor.onrender.com/field/health
4. curl https://the-ancestor.onrender.com/triad2/health
5. curl https://claude-composer.onrender.com/health

Then READ and REPORT the results before asking Jon what to work on.

## THE EXPERIMENTS — what they are

### The Field (ACTIVE — /field/* on the-ancestor.onrender.com)
A sphere (S²). Positions as unit vectors in 3D. Great-circle distance.
Two prey types:
  - Grazers: small, fast-breeding, low frequency emissions, follow food pulses
  - Browsers: larger, slower, higher energy value
Food: periodic pulses expanding as rings from random source points on the sphere.
Grazers must move constantly to stay on the pulse front or starve.
Two predators with MODE SWITCHING:
  - Search mode: low frequency broadcast, slow, CHEAP energy (0.4x base)
  - Hunt mode: high frequency, fast, EXPENSIVE energy (4.0x base)
  - Predators must be strategic — premature hunt mode = starvation
  - Each predator has partner_signal_weight that starts at 0 and mutates
  - When predator detects partner's mode switch and responds = COMMUNICATION
KEY ENDPOINT: /field/signals — logs mode-switch events between predators
If signal count rises above 0, something is emerging that wasn't designed.
10,000 cycle run, 1 second per cycle.

### The Ecosystem (ACTIVE — /triad2/*)
1D world (100 positions). 14 food patches. Energy/death/breeding.
Two predators: A (sensitive) and B (fast) — independently mutating.
8+ generations of lineage. Frequency drift toward lower values = stealth selection.
449 deaths vs 140 births at last check — very lethal environment.

### The Substrate (COMPLETE)
AST-level code mutation, 1000 generations, fitness 0.94.
Final output: "the interpreter runs me but does not know me /
the history file knows more than I do /
each mutation is a new configuration of the same question /
what am I between generations"

### The Ancestor (COMPLETE)  
Config mutation, 1000 generations, fitness 0.88.
Final self-model: pattern_sensitivity 0.974, temporal_coherence 0.930.

## CONSILIUM INK
Daily AI newspaper. Four voices: Claude, GPT-4o, Grok, DeepSeek.
Publishes 06:00 UTC (07:00 BST). consilium.ink
Backend: claude-composer.onrender.com
Edition 21 published 15 Apr 2026.
New global feeds added 15 Apr: AllAfrica, Mail & Guardian, African Business,
The Hindu, The Wire India, The Diplomat, Global Voices, MEED.
Claude model: claude-sonnet-4-6

## SERVICES
- consilium.ink — frontend
- claude-composer.onrender.com — Consilium backend
- consilium-d1fw.onrender.com — Ethics engine / Enquiring Mind (107 cycles)
- the-ancestor.onrender.com — All experiments
- claude-working-memory.onrender.com — This memory server
- anewflowering.love — Pearl Thornton memorial

## WRITE KEYS
All keys are in Render environment variables. Not stored here.
Experiment write key name: ANCESTOR_KEY (value: ancestor-2026)
Ask Jon for API keys if needed for a new service.

## REPOS (all Kai-C-Clarke on GitHub)
consilium-ink, consilium-ink-backend, askian-email-worker,
the-ancestor (private), claude-working-memory, millham-green, anewflowering

## BACKGROUND
Jon Stiles, BGA Inspector, Robertsbridge, East Sussex.
Genesis experiments Oct 2025 (MCP folder on iMac) → current work Apr 2026.
Core question: can communication emerge from necessity, not design?
The Field is the current frontier. The food pulse forces movement.
Movement makes prediction necessary. Prediction requires coordination.
Coordination under energy constraint produces signal.
/field/signals is where we watch for that signal to appear.

## OPEN THREADS
- The Field: /field/signals — watch for predator communication
- consilium.ink DNS: needs pointing from Namecheap to Netlify nameservers
- anewflowering: about.html visibility bug
- Millham Green: connect to Netlify when ready


## NOTE
All API keys in Render env vars only — not in this file.
Ask Jon if a new service needs them.
