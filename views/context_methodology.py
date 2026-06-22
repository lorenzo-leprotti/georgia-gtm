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
    "This analysis was built with an AI-assisted workflow: specification first, deep "
    "research with traceable sources, cross-checking across tools, and a working app at "
    "the end. The process mattered as much as the conclusion, so it is described here in "
    "full."
)

st.subheader("How this was built")

st.markdown(
    "**Specification before code.** The project started with a written product "
    "requirements document: purpose, audience, success criteria, and an explicit "
    "out-of-scope line, all fixed before anything was built. The strategy drove the "
    "artifact rather than the reverse."
)

st.markdown(
    "**Deep research for every claim.** Site-level facts were gathered with Perplexity in "
    "deep-research mode, which returns answers with traceable citations. Every site and "
    "figure had to carry a dated, publicly accessible source before it could enter the "
    "dataset."
)

st.markdown(
    "**Cross-referencing across tools.** Claude handled reasoning, structuring the "
    "argument, and synthesis; Perplexity handled source-grounded fact-finding. Findings "
    "from each were checked against the other, and a dedicated reference-check pass caught "
    "and corrected several early figures (for example, a nuclear outage cost that was "
    "overstated by several times). No number survived that could not be traced to a source."
)

st.markdown(
    "**Built in Claude Code.** The app was developed in Claude Code, with the verified "
    "data kept in a portable CSV decoupled from the code so it can be reused or audited "
    "independently."
)

st.markdown(
    "**Tech stack.** Streamlit for the multi-page app, Python and pandas for the data "
    "layer, and pydeck for the map. Deployed to Streamlit Cloud, redeploying "
    "automatically from GitHub."
)

st.subheader("How the target list was built")

st.write(
    "The site list was built source-first in a fixed sequence. Inclusion criteria were "
    "defined before any site was added, so no site could be chosen to fit a conclusion. "
    "Every site required a named, dated source (no source, no row). Sites found closed or "
    "inactive were removed (three mills were dropped), weak citations were upgraded (the "
    "top target's source moved from a county social media post to dated trade press), and "
    "map coordinates were corrected against authoritative sources such as Global Energy "
    "Monitor and official facility records. Each surviving site was then scored on five "
    "dimensions (sector fit, confirmed scaffolding demand, recurrence of shutdowns, "
    "ownership structure, and whether demand is active now) and grouped into three tiers, "
    "each with a confidence level reflecting source quality."
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
