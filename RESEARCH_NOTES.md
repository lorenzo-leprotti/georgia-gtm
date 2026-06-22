# Research Notes: KEWAZO Georgia GTM

This file consolidates the working documents behind the app: the project scope, the
method used, the buyer model, the target list rationale, the market sizing math, and the
reference check that corrected several figures before they went into the app. The point is
not the conclusion alone, but that it was reached in a structured, verifiable way.

All site-level facts live in `data/sites.csv`, one row per site, with a source URL and date
per row. Nothing entered the app or the CSV without a source.

---

## 1. Scope

An interactive Streamlit app arguing that Georgia is KEWAZO's next US industrial expansion
market, built on first-hand Atlanta knowledge and deployed to Streamlit Cloud so it can be
screen-shared live or sent as a link.

The scope was deliberately bounded: scaffolding-intensive maintenance shutdowns in process
industries (pulp and paper, power generation) as the entry point, with the construction
boom as a timing wedge, rather than "anywhere industrial."

What the artifact is, and nothing more:
1. A clean app that reads as one argument top to bottom.
2. The methodology and strategy: the thesis, the buyer logic, the evaluation criteria, the
   entry sequence. This is the substance.
3. The map: Georgia targets plotted, color-coded by tier. The visual hero.

Out of scope: live data feeds, CRM integration, prediction models, invented precision. This
is a strategy artifact, not a product.

## 2. Method

Spec before build. The work started with a written scope (purpose, audience, success
criteria, what was explicitly out of scope) before any code, so the strategy drove the
artifact rather than the other way around.

Verification rules applied to every claim:
- No source, no row.
- Closed sites removed (three mills excluded after the summer 2025 closures).
- Rounded map coordinates corrected against authoritative sources.
- Confidence flagged per row.
- Weak sources flagged and upgraded (the top site's citation was moved from a social media
  post to trade press).

Tools: Claude for reasoning, structuring, and the spec; Perplexity (deep-research mode) for
source verification; a portable CSV for the data layer; Streamlit and pandas for delivery.

Honest boundaries: the buyer model is research-confirmed for the sector, not validated
inside KEWAZO. A few rows carry medium confidence (for example, the Rincon shutdown cadence
has no public schedule). Tier 3 sites are included for completeness, not as live targets.
These are flagged rather than hidden.

## 3. The buyer model

The buyer is dual, not single, so the go-to-market is two-sided:

- **Decision-maker: the corporate asset owner/operator** (Southern Company / Georgia Power,
  Georgia-Pacific, Clearwater Paper). Sets the shutdown plan and specs-in or approves which
  access solutions are used. This is where LIFTBOT gets standardized.
- **Operational buyer and deployment channel: the scaffold-access contractor**
  (BrandSafway, Apache, Turner, Brown and Root). Engaged under long-term service
  agreements; physically deploys LIFTBOT on site. Sell to and partner with them as the
  channel.

Two contracting structures:
- **Structure A (most large shutdowns):** owner to scaffold specialist directly. The
  owner's maintenance or turnaround manager issues RFPs to pre-qualified scaffold
  contractors under a preferred-vendor agreement or competitive bid.
- **Structure B (complex nuclear/petrochemical):** owner to turnaround management
  contractor (Brown and Root, Turner) to scaffold subcontractor. Nuclear sites (Vogtle,
  Hatch) require NRC-compliant contractors on pre-approved vendor lists.

**Georgia advantage:** both ends of the chain sit in metro Atlanta. Owners Georgia-Pacific
and Southern Company are Atlanta-HQ'd, and BrandSafway, the dominant US scaffold-access
contractor, is HQ'd in Atlanta (600 Galleria Pkwy SE, formerly an Alpharetta address). Most
industrial geographies force parallel owner and contractor conversations across multiple
travel days; in Atlanta both can happen in the same week. This is the strongest argument in
the analysis.

**Value anchor:** scaffolding installation is roughly 15-25% of total shutdown direct field
labor (up to 35-40% when access is planned reactively; AMECO 2023 puts scaffolding install
at ~20%). LIFTBOT reduces the material-handling portion by 40-70% (KEWAZO's documented
range; independent industrial deployments land closer to 40%). Cascaded through, that is
roughly an 8-14% reduction in total shutdown direct labor cost.

**Channel tension, surfaced not hidden:** contractors may bill by man-hour, so a
labor-cutting robot can look like a revenue threat. It is mitigated by labor shortages (they
cannot staff the jobs) and by owner spec-in/mandates, which reframe the contractor as a
channel partner. In practice this is harder than one paragraph suggests: an owner mandate
means writing LIFTBOT into the shutdown specification 12-18 months ahead, during outage
planning, so KEWAZO must influence the owner's planning cycle well before the contractor is
engaged. The practical path is a pilot at one Clearwater or GP mill that produces a
documented cost result the owner can reference in subsequent shutdown specifications.

Chevron Technology Ventures' strategic investment supports the owner-level adoption pattern.

## 4. Evaluation criteria

Each Georgia target is scored on five criteria:
1. **Sector fit:** process/shutdown industry (paper, power, chemical) high; discrete
   manufacturing (auto, aerospace) medium; new construction timing-only.
2. **Scaffolding intensity:** how much scaffold-heavy work the site needs.
3. **Recurrence:** scheduled shutdowns (recurring revenue) high; one-off build low.
4. **Owner type:** corporate owner-operator, ideally Atlanta-HQ'd, high; fragmented GC/EPC
   low.
5. **Timing trigger:** active shutdown cadence or active megaproject build now.

## 5. Targets and tiers

Sites sort into three tiers (the map's color-coding). The data is in `data/sites.csv`;
the rationale follows.

**Tier 1, entry pipeline (recurring, scaffolding-heavy shutdowns):**
1. **GP Brunswick Cellulose Mill.** Highest confidence. Annual April outage confirmed,
   roughly 1,000 external contractors mobilized, Atlanta-HQ owner (Koch/GP). Start here.
2. **Clearwater Paper Augusta Mill.** Three confirmed major outages in 2025; about \$16M in
   annual direct outage cost. Direct entry point.
3. **Plant Vogtle.** Four nuclear units staggered, producing a near-continuous outage
   calendar. Southern Company (Atlanta HQ). Requires the NRC-compliant contractor channel.
4. **Plant Hatch.** Two nuclear units on an alternating ~18-month cycle. Southern Nuclear /
   Georgia Power.
5. **Plant Bowen.** Four coal units all active through ~2038 per Georgia Power's 2025 IRP.
   Maximum remaining scaffolding runway.
6. **Plant Scherer.** Three of four units active through 2030+. Most powerful coal plant in
   North America.
7. **GP Savannah River (Rincon) Mill.** Large tissue mill with recurring outage windows;
   lower confidence on exact schedule (no public cadence).
8. **Plant Wansley.** Gas combined-cycle, less shutdown-intensive, but a new 1,453 MW CC
   plus 500 MW BESS broke ground April 2026, creating near-term construction scaffolding
   demand.

**Tier 2, timing wedge (active megaproject construction, non-recurring):** Hyundai
Metaplant, SK Battery Commerce, Hyundai-SK Battery (Bartow), Qcells Dalton and Cartersville,
Rivian Stanton Springs. Buyer is the EPC/GC, more fragmented. Near-term examples with live
scaffolding demand: HSBMA Bartow (over 90% complete in early 2026) and Rivian (vertical
build from spring 2026).

**Tier 3, adjacent and low priority:** Kia West Point, Gulfstream Savannah, Lockheed
Marietta, Meta and Microsoft data centers. Expansion optionality only. Retain approximate
coordinates; sufficient for Tier 3 weight.

Coordinates for the nine highest-weight sites were corrected from rounded estimates against
Global Energy Monitor, Wikipedia infoboxes, and official facility addresses before mapping.

## 6. Market sizing (bottom-up)

Rather than an unanchored aggregate, the sizing builds from confirmed and estimated
per-site outage costs at a 20% scaffolding labor share:

| Site | Annual direct outage cost (est.) | Scaffolding share (20%) |
|---|---|---|
| Clearwater Paper Augusta | \$16M (confirmed, Q3 2025 earnings) | \$3.2M |
| GP Brunswick Cellulose | \$10-15M (estimated; no public figure) | \$2-3M |
| GP Rincon | \$8-12M (estimated tissue mill) | \$1.6-2.4M |
| Plant Vogtle (4 units, ~18 mo) | ~\$53M/yr equivalent | \$10.6M |
| Plant Hatch (2 units, ~18 mo) | ~\$24M/yr equivalent | \$4.8M |
| Plant Bowen (4 units, every 3 yr) | ~\$20M/yr equivalent | \$4M |
| Plant Scherer (3 units, every 3 yr) | ~\$15M/yr equivalent | \$3M |
| Plant Wansley (gas CC, every 4 yr) | ~\$8M/yr equivalent | \$1.6M |
| **Total** | **~\$164M/yr in direct outage cost** | **~\$33M/yr in scaffolding labor** |

At a 40-70% LIFTBOT reduction, the ~\$33M in addressable scaffolding labor implies
**\$13-23M/yr in savings available to Georgia Tier 1 owners.** This \$164M floor is far more
defensible than the unanchored \$350M figure from the original draft, and showing the math
makes the pitch more credible.

Context: Georgia is consistently a top 3-5 US state in pulp and paper output and accounts
for roughly 21% of US pulp and paper exports (Georgia Grown). Three large mills closed
within 90 days in summer 2025 (GP Cedar Springs, IP Savannah, IP Riceboro), cutting the
active mill count to 8 statewide and the Tier 1 paper list from 6 to 3. The survivors are
larger and better-capitalized; this is consolidation, not collapse, and the analysis states
it rather than hiding it.

## 7. Reference check and corrections

A dedicated verification pass (June 22, 2026) caught several figures in the original draft
that were wrong. All were corrected before the app shipped:

| Item | Issue in original draft | Correction applied |
|---|---|---|
| LIFTBOT reduction | Stated as a flat 70% | KEWAZO's documented range is 40-70%; industrial deployments land near 40%. Changed to 40-70%, savings cascaded to 8-14% of total shutdown labor. |
| Paper mill outage spend | "\$50M at one mid-sized mill in a year" | The \$50M covers three Clearwater mills combined. Augusta alone is ~\$16M direct outage cost, implying ~\$3.2M scaffolding labor. |
| Aggregate market | "\$350M/yr" with no math | Replaced with the bottom-up build above (~\$164M/yr floor). |
| Vogtle outage cost | "\$50M to \$150M per refueling outage" | Overstated 3-5x. Reframed as \$300K-\$800K/day x 20-35 days = roughly \$16-28M per unit, consistent with NEI, IIR, and the Diablo Canyon \$42M / 34-day reference. |
| BrandSafway scale | Third-party DBs reported \$25.5B | That conflates BrandSafway with a parent entity. Use the company's own "\$5B+ revenue, ~40,000 employees" figure. |
| BrandSafway HQ | Listed as Alpharetta | Now 600 Galleria Pkwy SE, Atlanta. |
| GP / Georgia Power contracts | Implied as confirmed clients | No public contract names either as a BrandSafway client. Stated as commercially inferred, not confirmed. |

### Confidence notes

- **Solid:** GP Brunswick annual outage (Pulp and Paper Chronicle, Fastmarkets); corrected
  coordinates (Global Energy Monitor); Plant Wansley gas/coal split and new build; Bowen and
  Scherer operating units (Georgia Power 2025 IRP); scaffolding 20% share (AMECO 2023).
- **Medium, flagged:** GP Rincon shutdown cadence (no public schedule); Rincon scale claim
  (directory source, no primary GP confirmation); Meta and Microsoft data center capacity
  (aggregator/vendor sources, Tier 3 weight).
- **Verdict:** the strategy is directionally correct and commercially logical. The target
  set is real, the buyer model is structurally accurate, and the Atlanta geography is a
  genuine and rare sales-efficiency advantage. The residual risks are execution-side (long
  sales cycle, channel tension with BrandSafway, nuclear access requirements), not
  market-side.
