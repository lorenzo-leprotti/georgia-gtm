# PRD — KEWAZO Georgia GTM Strategy App

_Owner: Lorenzo Leprotti. Drafted 2026-06-21. Status: finalized scope, pre-build._

## 1. Purpose
An interactive Streamlit app arguing Georgia as KEWAZO's next US industrial expansion market, built on Lorenzo's on-the-ground Atlanta knowledge. A proactive R2 differentiator, deployed to Streamlit Cloud so it can be screen-shared live or sent as a link afterward.

## 2. Audience
- **Luca (peer, R2):** knows the GTM motion. Judges whether the thinking is real.
- **CEO (the real target):** older, non-technical, not impressed by code architecture. Impressed by polish and substance. The artifact is proof that "this person can build and deliver."

Design for the CEO's eye, defend for Luca's questions.

## 3. Success criteria
- Walkable in 3-5 minutes live; stands on its own if sent as a link.
- Demonstrates: commercial reasoning about US market entry, real Georgia ground knowledge, GTM capability, and the ability to build something impressive.
- The map reads as visually impressive to a non-technical viewer.
- Every factual claim survives a "where's that from" question.

## 4. What the artifact is (scope)
Three things, nothing more:
1. **Structure** — a clean app shell that reads as one argument top to bottom.
2. **Methodology + strategy (text)** — the thesis, the buyer logic, the ICP scoring rubric, the entry sequence. This is the substance.
3. **Map (the visual hero)** — Georgia targets plotted, color-coded by tier, hover detail. Gets the most polish.

Automation/execution stays a light subsection inside methodology: one hypothesized GTM flow, framed as Lorenzo's assumptions, to show delivery ability and that swapping a tool (Make ↔ n8n) is no barrier. Not over-built.

## 5. Core thesis
Georgia is KEWAZO's next US industrial market. Two parts:
- **Recurring process-industry base leads:** pulp & paper, power generation. Scheduled maintenance turnarounds = KEWAZO's repeatable, high-value, proven use case (same job shape as the Gulf Coast energy work).
- **Construction/manufacturing boom is the timing wedge:** Hyundai Metaplant, battery plants, Qcells, data centers. New capacity = scaffolding-heavy work now. This is the "why now," not the core target.

## 6. Buyer model (confirmed via research — see `KEWAZO_Georgia_Master_Research.md`)
Dual buyer, two-sided GTM:
- **Decision-maker = corporate asset owner/operator** (Southern Company / Georgia Power, Georgia-Pacific, Clearwater Paper). Sets the turnaround plan and specs-in / approves which access solutions are used. This is where LIFTBOT gets standardized.
- **Operational buyer / deployment channel = scaffold-access contractor** (BrandSafway, Apache, Turner, Brown & Root). Engaged under long-term service agreements; physically deploys LIFTBOT on site. Sell to and partner with them as the channel.
- **Two contracting structures:** (A) owner → scaffold specialist directly (most large TARs); (B) owner → turnaround management contractor → scaffold sub (complex nuclear/petrochemical).
- **Georgia advantage — both sides in metro Atlanta:** owners Georgia-Pacific and Southern Company are Atlanta-HQ'd, and BrandSafway, the dominant US scaffold-access contractor, is HQ'd in Alpharetta, GA. Both ends of the GTM are on Lorenzo's home ground.
- **Value anchor:** scaffolding is ~15-25% of total turnaround man-hours (up to 30-40% when access is reactive); LIFTBOT cuts ~70% of the material-handling portion.
- **Channel tension, resolved not hidden:** contractors may bill by man-hour, so a labor-cutting robot can look like a revenue threat. Resolved by labor shortages (they can't staff the jobs) and owner spec-in/mandates, which reframe the contractor as a channel partner.

Chevron Technology Ventures' strategic investment supports the owner-level adoption pattern.

## 7. ICP scoring rubric (visible logic in the app)
Score each Georgia target on five criteria:
1. **Sector fit** — process/turnaround industry (paper, power, chemical) high; discrete manufacturing (auto, aerospace) medium; new construction timing-only.
2. **Scaffolding intensity** — how much scaffold-heavy work the site needs.
3. **Recurrence** — scheduled turnarounds (recurring revenue) high; one-off build low.
4. **Owner type** — corporate owner-operator, ideally Atlanta-HQ'd, high; fragmented GC/EPC low.
5. **Timing trigger** — active turnaround cadence or active megaproject build now.

## 8. Target tiers (map color-coding)
- **Tier 1 — beachhead.** Recurring process turnarounds, corporate owners, mostly Atlanta-HQ'd. Pulp & paper (Georgia-Pacific, WestRock, Graphic Packaging, International Paper, Interfor); power (Southern Company / Georgia Power: Vogtle, Scherer, Bowen, gas plants).
- **Tier 2 — timing wedge.** Active megaproject construction: Hyundai Metaplant, battery plants, Qcells, Rivian (verify status). Buyer is EPC/GC, more fragmented. Urgency story.
- **Tier 3 — adjacent, low priority.** Kia West Point, Gulfstream, Lockheed, metro Atlanta data centers. Expansion optionality only.

## 9. Out of scope
No live data feeds. No real CRM integration. No invented precision. No prediction models. Strategy artifact, not a product.

## 10. Data requirements (gating step — nothing builds before this)
Every site and figure verified in Perplexity with source + date before it enters the app. Data lives in a portable **`sites.csv`** (one row per site, source + date per row), decoupled from code so any build can reuse it. Unverified = not in the file. Schema and research prompt in `DATA_RESEARCH_PROMPT.md`. Buyer-chain, turnaround research, coordinate corrections, and source-quality audit in `KEWAZO_Georgia_Master_Research.md`.

## 11. Tech
- Streamlit, Python. Verified data isolated in a portable `sites.csv`, read at load (not hardcoded).
- Map via a good-looking, Streamlit-friendly lib (pydeck or plotly), chosen for visual quality.
- Deploy: Streamlit Cloud from GitHub. Pinned `requirements.txt`.
- Old files (app.py, gtm_data.py, map_preview.html) = reference only, untrusted data.

## 12. Build milestones (each a stop-and-verify gate)
1. PRD sign-off ✅
2. Perplexity research run + bucketed, sourced data
3. `sites.csv` saved + spot-checked
4. App shell + navigation
5. Map section (hero — most polish)
6. Strategy + methodology text
7. Light automation subsection
8. Polish pass
9. Deploy to Streamlit Cloud

## 13. Risks
- **Data accuracy** — main risk. Mitigated by verification gates.
- **Live-demo failure** — mitigated by the deployed link fallback.
- **Scope creep** into a fake product — hold the out-of-scope line.
- **Map effort imbalance** — must look impressive without sacrificing the argument.
