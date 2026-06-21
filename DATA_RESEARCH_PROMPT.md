# Perplexity research prompt — KEWAZO Georgia targets

_Paste the block below into Perplexity (use a Pro / deep research mode if available). Goal: a verifiable, bucketed, mappable target list + buyer-chain confirmation. Every fact must carry a source and date._

---

**Context.** I'm building a go-to-market market-entry analysis for a company called KEWAZO. KEWAZO makes LIFTBOT, a battery-powered robotic material hoist that automates the transport of scaffolding material on industrial sites, cutting scaffolding labor (man-hours) by up to ~70%. Its strongest, proven use case is scaffolding-intensive maintenance turnarounds at process plants (energy, petrochemical, pulp & paper, power, chemical). The likely buyer is the corporate asset owner/operator that owns and runs the plant. I am assessing the U.S. state of Georgia as the next expansion market.

**Task.** Identify and bucket the most relevant industrial and construction sites in Georgia, USA. Only include significant sites; exclude small facilities.

**For every site, return these fields:**
- Site name
- Owner/operator company, and that company's corporate HQ city
- Facility location (city + county) and approximate latitude/longitude (for mapping)
- Sector (e.g., pulp & paper, power generation, chemical, automotive, battery, solar, aerospace, data center)
- Scale indicator (production capacity, output, employee count, or capital investment in USD)
- Scaffolding / turnaround relevance: does the site run scheduled maintenance turnarounds? How scaffolding-intensive is it? How often do turnarounds occur?
- Status: operating / under construction / planned (with timeline if under construction)
- Source URL + date of the information

**Bucket the results into three tiers:**

- **Tier 1 — Recurring process-industry plants with scaffolding-heavy turnarounds.** Pulp & paper and power generation are the priority. Specifically look for: Georgia-Pacific, WestRock, Graphic Packaging, International Paper, and Interfor mills in Georgia; and Southern Company / Georgia Power plants (e.g., Plant Vogtle, Plant Scherer, Plant Bowen, major gas plants). Emphasize owners headquartered in Atlanta.
- **Tier 2 — Active megaproject construction with large near-term scaffolding demand.** E.g., Hyundai Metaplant, associated EV battery plants, Qcells solar manufacturing. Include Rivian (Stanton Springs) only with its current verified status, since it has had delays.
- **Tier 3 — Large adjacent industrial/manufacturing sites with lower scaffolding-maintenance intensity.** E.g., Kia (West Point), Gulfstream (Savannah), Lockheed Martin (Marietta), major metro-Atlanta data centers.

**Also answer these two questions, with sources:**
1. In a typical Georgia pulp/paper or power-plant turnaround, who contracts for and physically performs the scaffolding work — the plant owner directly, or a specialized industrial-services / scaffold-access contractor (e.g., BrandSafway, Apache Industrial Services)? Describe the contracting chain.
2. Roughly what share of total turnaround man-hours is scaffolding/access work, and what is the typical turnaround frequency per plant (every how many years)?

**Output format.** Return the sites as a single CSV (one row per site, all tiers in the same file, distinguished by the `tier` column) so it can be saved directly as `sites.csv` and read by any build. Use exactly these column headers, in this order:

`tier,site_name,owner_company,owner_hq_city,city,county,latitude,longitude,sector,scale_indicator,scaffolding_relevance,turnaround_frequency,status,construction_timeline,source_url,source_date,confidence`

Rules for the CSV:
- One row per site. `tier` is 1, 2, or 3.
- `latitude` / `longitude` = approximate facility coordinates (decimal degrees) for mapping.
- `scaffolding_relevance` = short phrase (e.g., "high — recurring TARs", "low — discrete assembly").
- `confidence` = high / medium / low, reflecting how well-sourced and current the row is.
- Quote any field that contains commas.
- Every row must have a `source_url` and `source_date`. No source = do not include the row.

After the CSV, answer the two buyer-chain questions in prose with sources (these go in a separate notes file, not the CSV). Explicitly flag anything uncertain, outdated, or unverifiable.

---

_After Perplexity returns: save the CSV as `sites.csv`, spot-check the Tier 1 owners and the Rivian status yourself, drop any low-confidence rows you can't stand behind, and that file becomes the reusable data layer for the Streamlit build (and anything else)._
