# How this was built

A short account of the method behind this analysis. The point is not the conclusion alone, but that it was reached in a structured, verifiable way.

## The question
Could Georgia be KEWAZO's next US industrial market, and which sites would you target first? To keep it sharp, the scope was deliberately bounded: scaffolding-intensive maintenance turnarounds in process industries (pulp & paper, power) as the beachhead, with the construction boom as a timing wedge, rather than "anywhere industrial."

## Approach: spec before build
Started with a PRD, not code. Defined purpose, audience, success criteria, scope, and what was explicitly out of scope, before anything was built. This forced the strategy to drive the artifact, not the other way around.

## Baseline thesis and assumptions
Two-part thesis: recurring process-industry turnarounds lead (repeatable, proven use case), and new manufacturing construction is the urgency layer. The core working assumption was the buyer model: who actually decides and who deploys. This was held as an explicit assumption, then tested, not asserted.

## Verification
Every factual claim was verified in a dedicated research pass with a source and date attached. Rules applied: no source, no row; closed sites removed (three mills excluded); rounded map coordinates corrected against authoritative sources; confidence flagged per row; weak sources flagged and upgraded (the top site's citation was moved from social media to trade press). A source-quality audit records what is solid versus still soft.

## Tools
- Reasoning, structuring, and the PRD: conversational AI (Claude).
- Source verification and fact-finding: Perplexity, deep-research mode.
- Data layer: a portable CSV, one row per site, decoupled from code so any build reuses it.
- Delivery: Streamlit (this app), Python/pandas for the data.

## The GTM model
The buyer is dual, not single. The asset owner (Georgia Power, Georgia-Pacific, Clearwater) specs-in and approves; the scaffold-access contractor (BrandSafway, Apache) deploys on site under long-term service agreements. Both ends sit in metro Atlanta. Value was quantified: scaffolding is ~15-25% of total turnaround labor, and a ~70% cut in material-handling translates to roughly a 10-17% reduction in total turnaround direct labor. Targets were scored on a five-criterion ICP rubric (sector fit, scaffolding intensity, recurrence, owner type, timing) and sorted into three tiers.

## What is assumed vs confirmed
Honest boundaries: the buyer model is research-confirmed for the sector, not validated inside KEWAZO. A few rows carry medium confidence (for example, the Rincon turnaround cadence has no public schedule). Tier 3 sites are included for completeness, not as live targets. These are flagged rather than hidden.
