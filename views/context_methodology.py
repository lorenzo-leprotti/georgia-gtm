import streamlit as st
import pandas as pd


@st.cache_data
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
    "Scaffolding typically accounts for 15 to 25 percent of total labor on a maintenance "
    "shutdown, rising to 35 to 40 percent when access is planned reactively. KEWAZO's "
    "documented range for LIFTBOT is a 40 to 70 percent reduction in material-handling "
    "labor, with industrial deployments typically closer to 40 percent. That translates "
    "to an 8 to 14 percent reduction in total shutdown direct labor cost. For asset owners "
    "running multi-million-dollar maintenance budgets, that is a board-level number."
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
    "it on site (BrandSafway, headquartered in Alpharetta) are both local. This is "
    "unusual and materially reduces the cost of building both the owner relationship "
    "and the deployment channel at the same time."
)

st.header("Methodology")

st.write(
    "The research followed a source-first approach. Inclusion criteria were defined "
    "before any site was added: operating industrial facilities in Georgia with confirmed "
    "or likely scaffolding-intensive maintenance operations. Three rules applied throughout:"
)

st.write(
    "**No source, no row.** Every site in this analysis requires a named, dated, "
    "publicly accessible source to be included. Sites verified only through informal "
    "or unattributable sources were excluded."
)

st.write(
    "**Closed or inactive sites excluded.** Three mills were removed during verification "
    "after being found inactive or permanently closed."
)

st.write(
    "**Precision over approximation.** Map coordinates were corrected against authoritative "
    "sources including Global Energy Monitor, Wikipedia facility infoboxes, and official "
    "facility addresses. Citations were upgraded where possible; the primary source for "
    "the top target site was moved from a county government social media post to a dated "
    "trade press article."
)

st.write(
    "Each site was evaluated on five criteria: fit for scaffolding-intensive maintenance "
    "work, confirmed demand for scaffolding access, frequency of recurring shutdowns, "
    "ownership structure (corporate owner-operators receive higher weight than fragmented "
    "contractors), and whether active demand is confirmed now. Targets were grouped into "
    "three tiers based on their overall score."
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

sources = df[["site_name", "source_url", "source_date", "confidence"]].copy()
sources.columns = ["Site", "Source", "Date", "Confidence"]

st.dataframe(
    sources,
    column_config={
        "Source": st.column_config.LinkColumn("Source"),
    },
    use_container_width=True,
    hide_index=True,
)

st.divider()
st.caption("Lorenzo Leprotti · June 2026 · Built with Streamlit + pydeck")
