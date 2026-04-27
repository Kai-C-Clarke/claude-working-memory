# Thought Map — 27 April 2026

## FIELD EXPERIMENT — SHELVED PENDING MACOS

### Status at shelving (27 Apr)
- Cycle ~65,340 | Generation 726
- avg_field_sensitivity: 0.4369 (declining)
- bm_trend: -0.01408 (negative)
- Silent Hunter strategy won — cannibalism marginally beating coordination
- Energy pool ~11,000 — stable on trickle

### Key result
Experiment produced a REAL result: Silent Hunter strategy won.
In a world where cannibalism ≈ coordination in reward, evolution selects for
low emission + low sensitivity. Not a failure — genuine finding about
prerequisite conditions for communication emergence.

### Why shelved
Experiment needs to restart from Stage 1 chemistry, not Stage 5 metabolism.
We started with entities already having metabolism, movement, reproduction.
Real emergence starts from self-replicating molecules, energy gradients,
no entities at all. Requires MacMiniMonster compute.

### v2.8 features (current codebase)
- Persistent save/load to /mnt/data/field_state.json
- Autosave every 1000 cycles
- Cooperative chain bm measurement (signal→partner→kill)
- social_bm metric
- Grazer flocking + flee response
- Cannibalism with energy threshold
- Coordination bonus (1.8x) drawn from energy pool
- Vent eruptions (0.05% probability per cycle)
- Trophic pyramid: 60 hunters max, 1500-4000 grazers, 30 blooms
- Energy trickle: 500/cycle
- All energy leaks fixed
- Metrics: avg_field_sensitivity, avg_dist_to_grazer, cannibal_kills, 
  coord_kills, pct_coordinating, social_bm

### Next experiment design
Start from Stage 1:
1. Chemistry only — no entities
2. Self-replicating molecules
3. Competition for building blocks emerges naturally
4. Membranes form
5. Metabolism emerges
6. Movement, sensing, signalling crystallise from physics
DO NOT design the outcome — let the environment produce it

---

## MAC MINI MONSTER

### Current situation (27 Apr 2026)
- M4 Mac Mini essentially unavailable — RAM shortage from AI datacentre demand
- M5 Mac Mini expected WWDC June 8 announcement
- M5 Pro: 18-core CPU, 4x AI performance vs M4, Fusion Architecture
- Available mid-late summer 2026 after announcement
- Cannot preorder yet — watch June 8
- Base storage expected 1TB (up from 256GB)
- Price expected ~$1,399+ for M5 Pro

### Storage strategy
- Base 1TB SSD sufficient for OS + active work
- External Thunderbolt 5 SSD (Samsung T9, ~£150) for working storage
- Large spinning disk for cold archive
- Much cheaper than Apple SSD upgrade, expandable

---

## WORKSHOP ASSISTANT — NEW PRIMARY PROJECT

### Concept
Voice-activated workshop assistant for glider inspection work:
- Voice input (local Whisper) — hands-free queries while working
- Camera — tool tracking, progress photos
- Aircraft knowledge base per registration
- AD/TN compliance cross-referencing
- Dictated observation recording → inspection report generation
- Shadow board camera — "You still have the AN spanner out"
- Google Drive integration for existing glider records

### Glider types to cover
- Ka 2b (Schleicher)
- ASK 13 (Schleicher)
- Ka 6E and Ka 6CR (Schleicher)
- K 8 (Schleicher)
- SHK-1 (Schleicher)
- Slingsby Swallow (T.38)
- Olympia 463 (T.45)
- DG-100G (DG Flugzeugbau)
- Me7
- Olympia 2b

### Data sources confirmed
Schleicher TN pages (individual pages per type):
- ASK 13: alexander-schleicher.de/en/tm-lta-wa/tm-flugzeuge/ask-13-technische-mitteilungen/
- Ka 6: alexander-schleicher.de/en/tm-lta-wa/tm-flugzeuge/ka6-technische-mitteilungen/
- K 8: alexander-schleicher.de/en/tm-lta-wa/tm-flugzeuge/k8-technische-mitteilungen/
- AD summary PDFs at alexander-schleicher.de/wp-content/uploads/

Slingsby sources:
- LAA (Light Aircraft Association) — holds T.38 and T.45 type approvals
- Slingsby Owners Club — member AD archives
- EASA AD database — easa.europa.eu
BGA: unreliable/unhelpful

DG sources:
- dg-flugzeugbau.de — well organised, similar to Schleicher

### Planned data structure
workshop/documents/K13/ — PDFs dropped into Claude Local workspace
workshop/documents/K6/
workshop/documents/K8/
etc.
Claude Local reads, extracts structured AD data → JSON knowledge base
Fields: AD number, date, applicability, what to inspect, interval, compliance

### Next steps
1. Visit each Schleicher type page, download PDFs
2. Search LAA for Slingsby T.38 and T.45 documentation
3. Search EASA AD database for all types
4. Search DG website for DG-100G
5. Build JSON knowledge base from extracted data
6. Build voice interface on MacMiniMonster

---

## DIGITAL PRESERVATION PROJECT — CONCEPT STAGE

### Concept
3D digital preservation of vintage gliders — complete digital twins
"Down to every last frame and tack" — buildable record for future generations
Preserve: geometry, materials, assembly techniques, aerodynamic reasoning,
inspector knowledge (what to look for, what fails, what was clever)

### 3D scanning options
- iPhone LiDAR (free if you have iPhone 15/16 Pro) — good starting point
- Revopoint RANGE 3 (~£600-800) — good for large objects
- Artec Leo/Eva (£10,000+) — professional/museum grade
- Photogrammetry (free software like Meshroom) — surprisingly accurate

### File sizes
- Full glider at archival quality: 50-100GB
- 4TB external drive handles 40-80 gliders
- Storage not the expensive part — scanner and time are

### Contacts to pursue
- Aviation Heritage UK (aviationheritageuk.org) — representative body for
  UK aviation museums, formerly BAPC, makes grants to member groups
  Worth contacting — may have existing digitisation programme

---

## CLAUDE LOCAL — CURRENT STATE

### Features working
- Workspace folder with recursive folder scanning
- PDF support (sent as base64 document blocks)
- Image support (jpg/png/gif/webp)
- Write-back to workspace files
- Toast notifications for new files
- @path syntax for file injection
- Memory loads from GitHub at startup
- Autosave to working memory server
- Token + cost tracking

### Known issues
- autosave indicator shows "undefined" (cosmetic)
- Drag-and-drop into browser blocked by macOS — use workspace folder

### File locations (Jon's Mac)
- ~/Desktop/claude_local/server.py
- ~/Desktop/claude_local/public/index.html
- ~/Desktop/claude_local/workspace/ — drop files here
- ~/Desktop/claude_local/conversations.db

---

## PHILOSOPHICAL THREADS

### Matter as fossilised record
Jon's intuition: all matter absorbs a record of what it has encountered.
Dinosaur footprint = 140M years of encoded information.
Gate impression in hedge = physical alteration encoding presence.
Connects to Bohm's implicate order.
Thermodynamic entropy = information dispersed not destroyed.
Universe as perfect recording medium — we lack the playback equipment.

### Quantum entanglement and time
Block universe / eternalist view — past, present, future all equally real.
Transactional interpretation — quantum events as handshakes between
waves running forward and backward in time.
Jon's intuition: entanglement "running from big bang to end of universe
and in the present" — close to transactional interpretation.

### The trophic pyramid insight
Jon's insight: use Earth's actual ratios because they work.
10,000 plant : 1,000 herbivore : 100 predator.
Earth figured this out 4 billion years ago — hard to argue with.
The trickle (8 units/cycle) is the fundamental constraint that shapes
the whole pyramid. Too much = Garden of Eden. Too little = extinction.
The narrow band between is where complexity lives.

### Communication prerequisites (from experiment)
1. Prey must be genuinely uncatchable alone
2. Coordination benefit must exceed emission cost
3. Cannibalism must be LESS rewarding than cooperation
4. Signal channel must stay rich enough to find partners
If any condition fails, Silent Hunter wins.

---

## OPEN THREADS
- Workshop assistant: data gathering next (Schleicher, Slingsby, DG)
- Mac Mini M5 Pro: watch WWDC June 8
- Field experiment: shelved until MacMiniMonster
- Digital preservation: contact Aviation Heritage UK
- Estate: HMRC SA900 call still pending
- Millham Green: conversation engine still priority when ready
- The Circle: circle_memories.db backed up to external drive
  (Railway account deleted — The Circle runs locally only)
- consilium.ink: field.html needs updating with v2 results

