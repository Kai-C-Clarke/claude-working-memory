# Thought Map Update — 23 April 2026

## The Ancestor — Key Insights (NOT YET BUILT)

### 1. Somatic Mutation
Current code mutates genomes only at breeding (offspring inherit with variation).
Missing: random mid-life changes to living individuals.
- Most will be harmful — individual dies
- Occasional breakthroughs — individual survives, breeds, passes on novel trait
- This is how genuinely novel capabilities emerge in nature
- Implementation: small probability per cycle of random genome parameter shift in any living hunter

### 2. Fundamental Locomotion Problem
**We handed hunters move_toward(). They didn't earn it.**

Real sequence in nature:
1. Random wiggling (Brownian-ish motion) — no target, just chemistry
2. Chemokinesis — wiggle MORE in presence of food signal, not toward it
3. Contact feeding (phagocytosis) — membrane deforms around chemical signal, closes. No hunt radius. Just overlap.
4. Directed movement evolves LATER if at all — nervous system coordinates existing movement, doesn't invent it

Current hunters have the answer given to them. Next rebuild: give only physics.

### 3. Movement Noise
Current movement too clean — always toward target.
Real organisms: motor noise, stumbling, accidental drift.
Stumbling INTO discoveries is not a bug. It's how life works.

### 4. Energy Conservation Bug
energy_pool drifted from 50,000 to 21,000,000 by cycle 600k.
Source: vent energy release not properly debited, or bloom energy gain not capped.
Fix before next rebuild.

### 5. bm Metric Assessment
bm hovering near zero at generation 5,000+.
Likely architectural — directed movement means hunters don't NEED signals to find food.
If movement is random, signals become genuinely valuable. bm should climb.

## Claude Local — Building Tonight
- Flask Python backend
- Web search via Anthropic API tool
- Local conversation history (SQLite or JSON)
- Prompt caching
- API key stored in environment variable
- Replaces claude.ai Pro subscription (~£150/month saving)

## Cost Resolution
- Cancel claude.ai Pro
- Keep all four API services (Anthropic, OpenAI, xAI, DeepSeek)
- Target: £40-50/month total
