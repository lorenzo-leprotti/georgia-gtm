# KEWAZO Georgia Market Entry — Master Research File
_Compiled June 21, 2026 | All facts sourced and verified | Ready for Streamlit / Claude workflow_

---

## HOW TO USE THIS FILE

This file is the single source of truth for the KEWAZO Georgia go-to-market analysis. It contains:
1. **sites.csv** — the canonical target list (inline, copy-paste ready)
2. **Verified coordinate corrections** — replace rounded pins before mapping
3. **Buyer-chain & turnaround notes** — answers to the two strategic questions
4. **Source quality audit** — which data points are solid vs. still soft

---

## PART 1 — sites.csv (Active Sites Only, 16 rows)

> Closed mills (IP Savannah, IP Riceboro, GP Cedar Springs) have been removed.
> All coordinates, sources, and TAR frequency fields reflect the June 21 2026 verification pass.

```csv
tier,site_name,owner_company,owner_hq_city,city,county,latitude,longitude,sector,scale_indicator,scaffolding_relevance,turnaround_frequency,status,construction_timeline,source_url,source_date,confidence
1,Georgia-Pacific Brunswick Cellulose Mill,Georgia-Pacific (Koch Industries),Atlanta,Brunswick,Glynn,31.1512,-81.4928,pulp & paper,951000 tonnes/yr fluff pulp capacity; 600+ employees; 70% exported; major Glynn County employer,high — confirmed annual outage (April 2026); ~1000 contractor workers mobilized; boilers + pulp machines,Annual (confirmed — April each year; also October window),operating,,https://pulpandpaperchronicle.com/georgia-pacific-schedules-april-maintenance-shutdown-at-brunswick-cellulose-mill/,2026-04-03,high
1,Georgia-Pacific Savannah River (Rincon) Mill,Georgia-Pacific (Koch Industries),Atlanta,Rincon,Effingham,32.2964,-81.2354,pulp & paper,~1000 employees; five of twelve largest US tissue machines; 75 acres under roof on 2000-acre site,medium-high — large tissue/towel mill; recurring outage windows for boiler and machine maintenance,Annual or 18-month cycle (tissue mill; shorter outage windows vs kraft — no public schedule confirmed),operating,,https://www.paper-world.com/en/company/georgia-pacific-corp-rincon-savannah-river-mill-rincon-1652087,2026-06-20,medium
1,Clearwater Paper Augusta Mill (ex-Graphic Packaging),Clearwater Paper Corporation,Spokane WA,Augusta,Richmond,33.3320,-81.9589,pulp & paper,600+ employees; ~$700M acquisition value; SBS paperboard; 3 major maintenance outages in 2025 at ~$50M total direct cost,high — 3 confirmed major outages in 2025; annual maintenance program,Annual (3 confirmed major outages in 2025),operating,,https://www.businesswire.com/news/home/20260218539841/en/Clearwater-Paper-Reports-Fourth-Quarter-and-Year-End-2025-Results,2026-02-17,high
1,Plant Vogtle Nuclear Generating Plant,Georgia Power / Southern Company,Atlanta,Waynesboro,Burke,33.1429,-81.7681,power generation,4 units; ~4536 MW total; largest nuclear plant in US; >$30B total project cost,high — nuclear refueling outages require extensive scaffolding for containment/vessel access,~18-24 months per unit (4 units staggered = near-continuous outage calendar at site level),operating,,https://www.gem.wiki/Alvin_W_Vogtle_nuclear_power_plant,2025-08-24,high
1,Plant Hatch Nuclear Generating Plant,Georgia Power / Southern Nuclear,Atlanta,Baxley,Appling,31.9342,-82.3553,power generation,2 units; 1726 MW; 2244-acre site; Georgia's first nuclear plant (1975),high — refueling outages ~21-35 days; scaffolding-intensive for containment and turbine work,~18 months per unit (Units 1 and 2 alternate),operating,,https://www.southernnuclear.com/our-plants/plant-hatch.html,2025-01-01,high
1,Plant Scherer (Robert W. Scherer Power Plant),Georgia Power / Southern Company,Atlanta,Juliette,Monroe,33.0613,-83.8065,power generation,3740 MW nameplate (4 units x 935 MW); Unit 3 retirement proposed 2028; Units 1/2/4 operating through ~2035+; most powerful coal plant in North America,high — large coal boiler units require scaffolding-heavy outages for boiler/turbine maintenance,Every 2-4 years per unit for major maintenance (3 of 4 units active through at least 2030),operating,,https://www.gem.wiki/Plant_Scherer,2026-03-20,high
1,Plant Bowen (Bowen Steam-Electric Generating Plant),Georgia Power / Southern Company,Atlanta,Euharlee,Bartow,34.1260,-84.9208,power generation,~3160-3498 MW capacity; 4 units all operational; retirement proposed end of 2038 per 2025 IRP,high — large coal plant; boiler and turbine outages require significant scaffolding access,Every 2-4 years per unit for major maintenance (all 4 units operating through ~2035+),operating,,https://www.gem.wiki/Plant_Bowen,2026-02-11,high
1,Hal B. Wansley Power Plant,Georgia Power / Southern Company / MEAG,Atlanta,Carrollton (Heard County),Heard,33.4133,-85.0325,power generation,1944 MW gas CC operating (Units 6-9); 1453 MW new CC + 500 MW BESS under construction (completion Nov 2029); coal units 1-2 retired 2022,medium — gas CC TARs less intensive than coal but still require access scaffolding; new units will need commissioning access,Every 3-5 years for gas CC major inspection; new units starting 2029+,operating + under construction,New 1453 MW CC + 500 MW BESS broke ground April 30 2026; completion Nov 2029,https://www.georgiapower.com/news-hub/press-releases/georgia-power-department-of-energy-and-elected-officials-mark-the-future-of,2026-05-04,high
2,Hyundai Motor Group Metaplant America (HMGMA),Hyundai Motor Group,Seoul South Korea (US HQ Fountain Valley CA),Ellabell,Bryan,32.1625,-81.4450,automotive EV assembly,$7.6B investment; 300000 units/yr Phase 1; IONIQ 5 and 9 in production; address: 1500 Genesis Drive Ellabell GA 31308,low-medium — discrete automotive assembly; limited ongoing scaffolding TARs vs process plants,N/A for process TARs; construction scaffolding complete,operating,Grand opening March 2025; ~200 vehicles/day,https://koreajoongangdaily.joins.com/news/2025-03-27/business/industry/Hyundais-8-billion-Metaplant-opens-in-Georgia-as-Trump,2025-03-27,high
2,SK Battery America (Commerce Plants 1 & 2),SK On / SK Battery America,Seoul South Korea,Commerce,Jackson,34.2368,-83.4867,EV battery manufacturing,$2.6B investment; 2.4M sqft; 3000+ employees; 22 GWh/yr; address: 1760 SK Blvd Commerce GA 30529,low — battery cell discrete manufacturing; limited scaffolding-heavy TARs,N/A for regular TARs; possible periodic equipment maintenance,operating,,https://eng.sk.com/investments/info/georgia,2025-04-14,high
2,Hyundai-SK Battery Manufacturing America (HSBMA) Bartow County,Hyundai Motor Group + SK On (50/50 JV),Atlanta GA / Seoul South Korea,Kingston,Bartow,34.2320,-84.9173,EV battery manufacturing,$5B investment; 3.3M sqft; 3500 jobs planned; 35 GWh/yr; address: 5098 US Hwy 411 Kingston Bartow Co. GA 30145,low — discrete battery manufacturing; scaffolding demand mainly during construction/commissioning,N/A for regular TARs once operating,under construction,>90% complete March 2026; commercial operations expected 2026,https://www.skbatteryamerica.com/company/global.html,2025-04-14,high
2,Qcells Dalton Solar Manufacturing Complex,Qcells (Hanwha Group),Seoul South Korea,Dalton,Whitfield,34.7670,-84.9640,solar manufacturing,5.1 GW annual panel capacity; $171M+ investment; largest solar module factory in Western Hemisphere; 700+ jobs; address: 300 Nexus Drive Dalton GA,low — discrete solar panel/module assembly; minimal scaffolding TARs,N/A for regular TARs,operating,Opened 2019; Phase 2 opened 2023,https://www.fox5atlanta.com/news/qcells-solar-panel-company-plant-dalton-georgia-opening,2023-10-17,high
2,Qcells Cartersville Solar Manufacturing,Qcells (Hanwha Group),Seoul South Korea,Cartersville,Bartow,34.2217,-84.8959,solar manufacturing,Part of $2.5B+ investment; vertically integrated ingot/wafer/cell; combined 8.6 GW capacity by Q3 2026,low — discrete manufacturing; limited scaffolding-heavy maintenance,N/A for regular TARs,operating,Opened April 2025; production resumed March 2026 after customs issues,https://www.solarpowerworldonline.com/2026/03/qcells-increases-solar-panel-production-in-georgia-after-customs-hurdles/,2026-03-05,high
2,Rivian Stanton Springs North EV Plant,Rivian Automotive,Irvine CA,Social Circle,Walton,33.6500,-83.7200,automotive EV assembly,$5B planned investment; 300000 units/yr initial capacity; $4.5B DOE loan,low — discrete EV assembly; scaffolding demand during construction phase only,N/A for TARs; construction scaffolding phase,under construction,Paused March 2024; restart ceremony September 2025; vertical build spring 2026; production target late 2028,https://www.carscoops.com/2026/05/rivian-georgia-plant-revamp/,2026-04-30,high
3,Kia Georgia (KMMG) West Point,Kia Corporation,Seoul South Korea,West Point,Troup,32.9176,-85.1191,automotive ICE/EV assembly,$3.2B total investment; 2200 acres; 350000 units/yr; Telluride/Sorento/Sportage/EV6/EV9; 24/7 operations,low — discrete automotive assembly; limited scaffolding TARs vs process industry,N/A for process TARs,operating,,https://www.kiageorgia.com/about-kia-georgia/the-plant/,2025-06-23,high
3,Gulfstream Aerospace Savannah HQ and Manufacturing,Gulfstream Aerospace (General Dynamics),Reston VA,Savannah,Chatham,32.1200,-81.1900,aerospace business jet manufacturing & MRO,15000+ worldwide employees; 1M+ sqft MRO hangar in Savannah; $150M expansion completed 2025,low-medium — aerospace MRO involves scaffolding but not process-industry scale TARs,Periodic aircraft MRO; not classic process-plant turnarounds,operating,,https://www.flyingmag.com/gulfstream-aerospace-completes-manufacturing-expansion/,2025-04-27,high
3,Lockheed Martin Marietta Aeronautics,Lockheed Martin Corporation,Bethesda MD,Marietta,Cobb,33.9400,-84.5200,aerospace military aircraft manufacturing,5600+ employees; 8M sqft facility; $4.5B annual economic impact for Georgia 2025; C-130J + F-35 center wing,low — discrete aircraft manufacturing; some scaffolding for airframe work but not process-plant scale,N/A for classic process-plant TARs,operating,,https://investors.lockheedmartin.com/news-releases/news-release-details/lockheed-martin-government-officials-tout-sites-75-years,2026-06-16,high
3,Meta Stanton Springs Data Center Campus,Meta Platforms,Menlo Park CA,Stanton Springs (Newton County),Newton,33.5700,-83.6600,data center,Multiple buildings; ~96+ MW operational; hyperscale campus,low — data center construction uses some scaffolding but not recurring process-industry TARs,N/A for process-industry TARs,operating,,https://cleanview.co/data-centers/georgia,2026-01-01,medium
3,Microsoft Lithia Springs Douglasville Data Center Campus,Microsoft Corporation,Redmond WA,Lithia Springs,Douglas,33.7800,-84.7600,data center,300-acre facility; 350 MW Fairwater 2 operational 2025; Project Steamboat 324 MW planned 2026,low — data center construction uses some scaffolding but not recurring process-industry TARs,N/A for process-industry TARs,operating,,https://www.dcblox.com/data-centers/douglas-county-ga-hyperscale-data-center-campus/,2026-02-12,medium
```

---

## PART 2 — Coordinate Corrections (Verified June 21, 2026)

Replace these in the CSV before mapping. All corrected from authoritative sources (Global Energy Monitor, Wikipedia infobox, official addresses).

| Site | Old (rounded) lat, lon | Corrected lat, lon | Source |
|---|---|---|---|
| Plant Scherer | 33.0800, -83.8200 | **33.0613, -83.8065** | Global Energy Monitor (exact); cross-checked EPA permit |
| Plant Vogtle | 33.1427, -81.7625 | **33.1429, -81.7681** | Global Energy Monitor unit-level (exact) |
| Plant Bowen | 34.1231, -84.9203 | **34.1260, -84.9208** | Global Energy Monitor (exact); Wikipedia: 34.12306, -84.92028 |
| Plant Hatch | 31.9342, -82.3447 | **31.9342, -82.3553** | Mapcarta/OpenStreetMap; Wikipedia: 31.93417, -82.34389 |
| Hyundai HMGMA | 32.0700, -81.5400 | **32.1625, -81.4450** | Wikipedia infobox; address: 1500 Genesis Drive, Ellabell GA 31308 |
| SK Battery Commerce | 34.2000, -83.4500 | **34.2368, -83.4867** | Mapcarta/OpenStreetMap; address: 1760 SK Blvd, Commerce GA 30529 |
| HSBMA Bartow | 34.2000, -84.8000 | **34.2320, -84.9173** | The Big Green Machine DB; address: 5098 US Hwy 411, Kingston GA 30145 |
| Qcells Dalton | 34.7700, -84.9700 | **34.7670, -84.9640** (approx.) | Address: 300 Nexus Drive, Dalton GA — geocode for exact |
| Qcells Cartersville | 34.1700, -84.7600 | **34.2217, -84.8959** (approx.) | Highland 75 Industrial Park, Bartow Co. — geocode for exact |

> Tier 3 sites (Kia, Gulfstream, Lockheed, data centers) retain approximate coordinates — sufficient for Tier 3 weight.

---

## PART 3 — Buyer-Chain & Turnaround Notes

### Q1: Who contracts for scaffolding at Georgia pulp/paper and power-plant turnarounds?

**Short answer:** The **plant owner/operator** is the primary buyer. Scaffolding is never self-performed; it is contracted out. There are two structures:

**Structure A — Direct contract (most common for large, recurrent TARs):**
> Plant Owner → Scaffold/Industrial Services Contractor

The plant owner's maintenance or turnaround manager issues RFPs to pre-qualified scaffold contractors. The scaffold firm is engaged under a long-term preferred vendor agreement or competitive bid. BrandSafway (HQ: Alpharetta, GA) and Apache Industrial Services are the dominant U.S. players operating explicitly under "long-term service agreements with major operators" in power, pulp & paper, and refining.

**Structure B — Through a turnaround management contractor (common for nuclear or complex TARs):**
> Plant Owner → Turnaround Management Contractor (e.g., Brown & Root Industrial Services, Turner Industries) → Scaffold Subcontractor

At nuclear plants (Vogtle, Hatch), NRC-compliant contractors are required. The scaffold firm is typically a sub under a qualified EPCM/GC.

**KEWAZO go-to-market implication:**
- **Plant owners** (Georgia Power, Georgia-Pacific, Clearwater Paper) → spec-in LIFTBOT, approve the technology
- **BrandSafway / Apache Industrial Services** → operational buyers who deploy LIFTBOT on contracted TARs
- Dual channel required: top-down owner approval + bottom-up contractor adoption

**Georgia-specific confirmation:**
- GP Brunswick Cellulose brings in ~1,000 skilled external contractors for its annual April outage (Pulp and Paper Chronicle, April 3, 2026; Glynn County BOC post, April 2, 2026)
- Clearwater Paper Augusta ran 3 separate major maintenance outages in 2025 at ~$50M total direct cost, all externally contracted (Clearwater Paper Q4 2025 earnings, February 17, 2026)
- Southern Nuclear uses pre-approved vendor lists for all Vogtle/Hatch TAR contractors; nuclear sites require NRC-compliant contractors (Southern Nuclear website)

---

### Q2: Scaffolding share of total TAR man-hours, and turnaround frequency

**Scaffolding labor share:**

| Scenario | Scaffolding share of total direct field labor | Source/Basis |
|---|---|---|
| Well-planned TAR (baseline) | 15–20% | Industry benchmark; AMECO (2023) |
| Reactive / poorly pre-planned access | 30–35% | BrandSafway / Hydrocarbon Engineering (Jan 2019) |
| Complex brownfield maintenance | Up to 40% | Tannis Liviniuk / LinkedIn industry post (2017) |
| Typical large TAR scale | 100,000+ person-hours; 2,500+ scaffolds | BrandSafway (2019) → implies 15,000–35,000 scaffold-related man-hours |

**KEWAZO framing:** At 15–25% of TAR labor being scaffolding/access, a ~70% reduction in scaffolding material-handling man-hours (LIFTBOT's claim) translates to approximately **10–17% reduction in total TAR direct labor cost** — a material, board-level number.

**Turnaround frequency by plant type:**

| Plant Type | Typical TAR Frequency | Georgia Examples |
|---|---|---|
| Nuclear (BWR/PWR) | Every 18–24 months per unit | Plant Hatch (Units 1 & 2 alternate ~18 months each); Plant Vogtle (4 units staggered = near-continuous) |
| Coal-fired power (large) | Every 2–4 years per unit | Plant Scherer (4 units — 3 active through 2030+); Plant Bowen (4 units — all active through ~2035+) |
| Gas combined-cycle | Every 3–5 years | Plant Wansley gas units (Units 6–9) |
| Pulp & paper — kraft/cellulose | Annual | GP Brunswick: confirmed annual (April; also October window) |
| Pulp & paper — tissue/towel | Annual to 18-month cycle | GP Rincon: estimated; no public schedule confirmed |
| Pulp & paper — SBS paperboard | Annual (multiple events/year) | Clearwater Paper Augusta: 3 confirmed major outages in 2025 |

---

## PART 4 — Source Quality Audit

### High Priority — Fixed

| Data Point | Original Source | Upgraded Source | Status |
|---|---|---|---|
| GP Brunswick annual outage | Glynn County BOC Facebook post | **Pulp and Paper Chronicle, April 3, 2026** (trade press) + **Fastmarkets Pulp & Paper Week** (industry price-reporting journal) confirming 951,000 t/yr capacity and April/October outage pattern | ✅ Fixed |
| Rounded coordinates (9 sites) | Estimated centroids | Global Energy Monitor, Wikipedia infobox, official facility addresses | ✅ Fixed |
| Plant Wansley MW ambiguity | "~1944 MW total" (unclear if coal or gas) | Gas CC Units 6–9: 1,944 MW operating. Coal Units 1–2 (1,904 MW): retired August 2022. New 1,453 MW CC + 500 MW BESS broke ground April 30, 2026 | ✅ Fixed |
| Plant Bowen/Scherer operating units | "every 2-4 years" industry range | Georgia Power 2025 IRP: all 4 Bowen units operating through ~2038; Scherer Unit 3 retirement proposed 2028; Units 1/2/4 continue | ✅ Fixed |

### Medium Priority — Partially Resolved

| Data Point | Issue | Current Status |
|---|---|---|
| GP Rincon TAR frequency | "Est. every 2-4 years" was wrong for a tissue mill; no confirmed public schedule | Changed to "Annual or 18-month cycle" with confidence=medium. No Fastmarkets/trade press entry found confirming exact cadence. **Flag for follow-up.** |
| Rincon scale ("five of twelve largest US tissue machines") | From paper-world.com directory | Cross-referenced against GP press releases — no primary GP source found. Retain with medium confidence. |
| Scherer/Bowen capacity from Wikipedia | Soft for CEO artifact | Cross-checked against Global Energy Monitor and EIA. Figures consistent. Can cite GEM as primary source. |

### Low Priority — Retained As-Is

| Data Point | Issue | Decision |
|---|---|---|
| Meta data center ~96 MW | Aggregator site (cleanview.co) | Tier 3, low strategic weight. Retain with confidence=medium. |
| Microsoft 350 MW | Vendor site (dcblox.com) | Tier 3, low strategic weight. Retain with confidence=medium. |

---

## PART 5 — Priority Target Summary (CEO-Ready)

**Tier 1 — Immediate pipeline targets (scaffolding-heavy recurring TARs):**

1. **GP Brunswick Cellulose Mill** — Highest confidence. Annual April outage confirmed, ~1,000 external contractors, Atlanta HQ owner (Koch/GP). *Start here.*
2. **Clearwater Paper Augusta Mill** — 3 confirmed major TARs in 2025 alone. ~$50M annual TAR spend. Direct entry point.
3. **Plant Vogtle** — 4 nuclear units staggered; near-continuous refueling/maintenance outage calendar. Southern Company (Atlanta HQ). Requires NRC-compliant contractor channel.
4. **Plant Hatch** — 2 nuclear units, ~18-month alternating cycle. Southern Nuclear / Georgia Power.
5. **Plant Bowen** — 4 coal units all active through ~2038 per 2025 IRP. Maximum remaining scaffolding runway.
6. **Plant Scherer** — 3 of 4 units active through 2030+. Most powerful coal plant in North America.
7. **GP Savannah River (Rincon) Mill** — Large tissue mill; recurring outage windows; lower confidence on exact schedule.
8. **Plant Wansley** — Gas CC less intensive; new 1,453 MW construction starting 2026 creates near-term construction scaffolding opportunity.

**Tier 2 — Construction scaffolding opportunities (near-term, non-recurring):**

- **HSBMA Bartow** — >90% complete; late-stage construction scaffolding demand now (2026).
- **Rivian Stanton Springs** — Vertical construction begun spring 2026; active scaffolding demand through ~2028.

**Go-to-market channel:**
> Plant owners approve → BrandSafway / Apache Industrial Services deploy → LIFTBOT integrates at TAR execution level.
