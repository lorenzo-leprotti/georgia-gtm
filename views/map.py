import streamlit as st
import pandas as pd
import pydeck as pdk


@st.cache_data
def load_sites() -> pd.DataFrame:
    df = pd.read_csv("data/sites.csv")
    color_map = {
        1: [220, 53, 69, 210],
        2: [253, 126, 20, 210],
        3: [108, 117, 125, 180],
    }
    radius_map = {1: 9000, 2: 7000, 3: 5500}
    df["color"] = df["tier"].map(color_map)
    df["radius"] = df["tier"].map(radius_map)
    return df


df = load_sites()

st.title("Georgia: KEWAZO's Next US Industrial Market")
st.caption("A targeted GTM thesis · Lorenzo Leprotti · June 2026")
st.divider()

st.header("Target Map — Georgia Industrial Sites")

col_legend, col_map = st.columns([1, 5])
with col_legend:
    st.markdown("**TIER LEGEND**")
    st.markdown("🔴 **Tier 1** — Beachhead")
    st.caption("Recurring process TARs")
    st.markdown("🟠 **Tier 2** — Timing Wedge")
    st.caption("Active megaproject builds")
    st.markdown("⚪ **Tier 3** — Adjacent")
    st.caption("Expansion optionality")
    st.caption("Hover pins for detail")

with col_map:
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position=["longitude", "latitude"],
        get_color="color",
        get_radius="radius",
        radius_min_pixels=7,
        radius_max_pixels=22,
        pickable=True,
        auto_highlight=True,
        highlight_color=[255, 255, 255, 80],
    )
    view = pdk.ViewState(latitude=32.7, longitude=-83.3, zoom=6.1, pitch=0)
    tooltip = {
        "html": (
            "<div style='font-size:13px;line-height:1.6'>"
            "<b style='font-size:15px'>{site_name}</b><br>"
            "<span style='color:#aaa'>Owner: </span>{owner_company} <span style='color:#aaa'>({owner_hq_city} HQ)</span><br>"
            "<span style='color:#aaa'>Sector: </span>{sector}<br>"
            "<span style='color:#aaa'>TAR Frequency: </span>{turnaround_frequency}<br>"
            "<span style='color:#aaa'>Scaffolding: </span>{scaffolding_relevance}"
            "</div>"
        ),
        "style": {
            "backgroundColor": "#0a1628",
            "color": "#f8f9fa",
            "padding": "14px 16px",
            "borderRadius": "8px",
            "maxWidth": "380px",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
        },
    }
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view,
        tooltip=tooltip,
        map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
    )
    st.pydeck_chart(deck, use_container_width=True, height=520)

st.header("Target Breakdown & ICP Scoring")

tier1 = df[df["tier"] == 1][["site_name", "owner_company", "city", "sector", "turnaround_frequency", "confidence"]].copy()
tier2 = df[df["tier"] == 2][["site_name", "owner_company", "city", "sector", "status", "confidence"]].copy()
tier3 = df[df["tier"] == 3][["site_name", "owner_company", "city", "sector", "confidence"]].copy()

t1_tab, t2_tab, t3_tab, rubric_tab = st.tabs(["Tier 1 — Beachhead", "Tier 2 — Timing Wedge", "Tier 3 — Adjacent", "ICP Scoring Rubric"])

with t1_tab:
    st.markdown("**Recurring process-industry turnarounds. Corporate owners, mostly Atlanta-HQ'd. These are the pipeline.**")
    tier1.columns = ["Site", "Owner", "City", "Sector", "TAR Frequency", "Confidence"]
    st.dataframe(tier1, use_container_width=True, hide_index=True)

with t2_tab:
    st.markdown("**Active megaproject builds. Urgency story — construction scaffolding now, not recurring TARs.**")
    tier2.columns = ["Site", "Owner", "City", "Sector", "Status", "Confidence"]
    st.dataframe(tier2, use_container_width=True, hide_index=True)

with t3_tab:
    st.markdown("**Adjacent. Included for completeness, not as live targets. Discrete manufacturing — limited scaffolding TARs.**")
    tier3.columns = ["Site", "Owner", "City", "Sector", "Confidence"]
    st.dataframe(tier3, use_container_width=True, hide_index=True)

with rubric_tab:
    st.markdown("**Five criteria scored per target. Tier 1 sites score high on all five.**")
    rubric = pd.DataFrame([
        {"Criterion": "Sector Fit", "High (3)": "Process/turnaround industry — pulp & paper, power, chemical", "Medium (2)": "Discrete manufacturing with some maintenance", "Low (1)": "New construction only, no recurring TARs"},
        {"Criterion": "Scaffolding Intensity", "High (3)": "Confirmed scaffolding-heavy outages (boilers, turbines, vessels)", "Medium (2)": "Some scaffolding in periodic maintenance", "Low (1)": "Minimal — clean room / discrete assembly"},
        {"Criterion": "Recurrence", "High (3)": "Annual or 18-month turnaround cycle (recurring revenue)", "Medium (2)": "Multi-year cycle, infrequent", "Low (1)": "One-off build — no repeat"},
        {"Criterion": "Owner Type", "High (3)": "Corporate owner-operator, ideally Atlanta-HQ'd", "Medium (2)": "Corporate owner, remote HQ", "Low (1)": "Fragmented GC/EPC, no clear owner-level relationship"},
        {"Criterion": "Timing Trigger", "High (3)": "Active TAR cadence confirmed or active megaproject build now", "Medium (2)": "Known cadence, no confirmed near-term outage", "Low (1)": "No confirmed near-term activity"},
    ])
    st.dataframe(rubric, use_container_width=True, hide_index=True)
