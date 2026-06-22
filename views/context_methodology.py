from urllib.parse import urlparse

import streamlit as st
import pandas as pd


def load_sites() -> pd.DataFrame:
    return pd.read_csv("data/sites.csv")


df = load_sites()

st.title("Georgia: KEWAZO's Next US Industrial Market")
st.caption("A targeted market entry analysis · Lorenzo Leprotti · June 2026")
st.divider()

st.header("Context")

st.write(
    "KEWAZO makes LIFTBOT, a robotic system that handles material transport during "
    "industrial scaffolding operations. When large industrial facilities (power plants, "
    "paper mills, chemical plants) shut down equipment for scheduled maintenance, they "
    "bring in hundreds of external contractors to erect and dismantle scaffolding around "
    "the machinery. LIFTBOT automates the most labor-intensive part of that process: "
    "lifting and moving materials up and through the structure, a task that currently "
    "requires large crews and carries significant safety risk."
)

st.write(
    "This analysis argues that Georgia is KEWAZO's next US market entry target. The case "
    "has two parts: a base of process-industry facilities (paper mills and power plants) "
    "that run scheduled maintenance shutdowns on annual to 18-month cycles (the recurring, "
    "core opportunity), and a manufacturing construction boom (Hyundai, battery plants, "
    "solar factories) that creates near-term scaffolding demand during the build phase "
    "(the timing driver). Both are documented with verified sources."
)

st.write(
    "Georgia's particular advantage: both sides of the commercial relationship are "
    "headquartered in metro Atlanta. The asset owners who would approve LIFTBOT "
    "(Georgia Power, Georgia-Pacific) and the scaffolding contractors who would deploy "
    "it on site (BrandSafway, headquartered in Atlanta) are both local. This is "
    "unusual and materially reduces the cost of building both the owner relationship "
    "and the deployment channel at the same time."
)

st.header("Methodology")

st.write(
    "The research followed a source-first process applied in a fixed sequence. Each step "
    "below had to pass before a site advanced to the next."
)

st.markdown(
    "**Step 1. Define inclusion criteria before adding any site.** "
    "A site qualified only if it was an operating industrial facility in Georgia with "
    "confirmed or likely scaffolding-intensive maintenance operations. The criteria were "
    "fixed first so that no site could be added to fit a conclusion."
)

st.markdown(
    "**Step 2. Source every site (no source, no row).** "
    "Every site required a named, dated, publicly accessible source to be included. "
    "Sites known only through informal or unattributable sources were not added."
)

st.markdown(
    "**Step 3. Verify and exclude.** "
    "Sites found closed or inactive were removed (three mills were dropped during this "
    "step). Citations were upgraded where possible: the primary source for the top target "
    "site was moved from a county government social media post to a dated trade press "
    "article. Map coordinates were corrected against authoritative sources including "
    "Global Energy Monitor, Wikipedia facility infoboxes, and official facility addresses."
)

st.markdown(
    "**Step 4. Score each site on five evaluation dimensions.** "
    "Every surviving site was scored on the same five dimensions:"
)

st.markdown(
    "1. Fit for scaffolding-intensive maintenance work.\n"
    "2. Confirmed demand for scaffolding access.\n"
    "3. Frequency of recurring shutdowns.\n"
    "4. Ownership structure (corporate owner-operators are weighted higher than "
    "fragmented contractors).\n"
    "5. Whether active demand is confirmed now."
)

st.markdown(
    "**Step 5. Group into tiers by score.** "
    "Sites were grouped into three tiers based on their overall score across the five "
    "dimensions. Each site also carries a confidence level reflecting the quality of its "
    "primary source (defined in the Sources section below)."
)

st.subheader("Limitations")

st.write(
    "The buyer-side model (who approves the technology at the owner level, who deploys "
    "it through the contractor channel) is confirmed through industry research for the "
    "sector, but has not been validated with KEWAZO internally. One site (Georgia-Pacific "
    "Rincon) carries medium confidence: no public maintenance schedule has been identified. "
    "Tier 3 sites are included for completeness and are not active targets."
)

st.header("Sources")

st.write(
    "One primary source per site, verified between June 2025 and June 2026. "
    "Confidence reflects the quality of the primary source: high means trade press, "
    "official filings, or authoritative databases; medium means industry directories "
    "or secondary aggregators."
)

def _domain(url: str) -> str:
    netloc = urlparse(url).netloc
    return netloc[4:] if netloc.startswith("www.") else netloc


rows = ["| Site | Source | Date | Confidence |", "| --- | --- | --- | --- |"]
for _, r in df.iterrows():
    link = f"[{_domain(r['source_url'])}]({r['source_url']})"
    rows.append(f"| {r['site_name']} | {link} | {r['source_date']} | {r['confidence']} |")

st.markdown("\n".join(rows))

st.divider()
st.caption("Lorenzo Leprotti · June 2026 · Built with Streamlit + pydeck")
