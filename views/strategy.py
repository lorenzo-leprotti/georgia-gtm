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

# ── HERO ────────────────────────────────────────────────────────────────────
st.title("Georgia: KEWAZO's Next US Industrial Market")
st.caption("A targeted GTM thesis · Lorenzo Leprotti · June 2026")
st.divider()

# ── THESIS ──────────────────────────────────────────────────────────────────
st.header("The Thesis")

col1, col2 = st.columns(2)
with col1:
    st.info(
        "**Part 1 — The Base**\n\n"
        "Georgia's process-industry base drives recurring revenue. Pulp & paper mills "
        "and power plants run scheduled maintenance turnarounds on annual to 18-month "
        "cycles. This is exactly KEWAZO's proven use case — the same job shape as Gulf "
        "Coast energy work. Atlanta-headquartered owners (Georgia Power, Georgia-Pacific) "
        "control both sides of the spec-in decision."
    )
with col2:
    st.info(
        "**Part 2 — The Timing Wedge**\n\n"
        "A $20B+ manufacturing boom creates urgency now. Hyundai Metaplant, battery "
        "plants, Qcells, Rivian — active megaproject construction means scaffolding-heavy "
        "builds today. This is the \"why now,\" not the core thesis. It opens the door; "
        "the turnaround base keeps it open."
    )

c1, c2, c3, c4 = st.columns(4)
stats = [
    ("Tier 1 beachhead targets", "8"),
    ("Avg TAR cadence, top sites", "~Annual"),
    ("Scaffolding share of TAR labor", "15–25%"),
    ("LIFTBOT material-handling reduction", "~70%"),
]
for col, (lbl, num) in zip([c1, c2, c3, c4], stats):
    col.metric(lbl, num)

st.warning(
    "**The value anchor:** Scaffolding is ~15–25% of total turnaround direct labor "
    "(up to 35–40% when access is reactive). A ~70% reduction in scaffold "
    "material-handling translates to roughly **10–17% reduction in total TAR direct "
    "labor cost** — a board-level number for asset owners running multi-million-dollar "
    "outages."
)

# ── BUYER MODEL ─────────────────────────────────────────────────────────────
st.header("The Buyer Model")

st.markdown(
    "Georgia is unusual: **both ends of the GTM sit in metro Atlanta.** "
    "Asset owners who approve the technology and scaffold contractors who deploy it "
    "on site are both headquartered here."
)

col_a, col_arr1, col_b, col_arr2, col_c = st.columns([3, 0.5, 3, 0.5, 3])
with col_a:
    with st.container(border=True):
        st.caption("DECISION-MAKER")
        st.markdown("**Asset Owner / Operator**")
        st.write("Georgia Power · Southern Company · Georgia-Pacific · Clearwater Paper")
        st.caption("Specs-in LIFTBOT, sets the TAR plan, approves vendors. HQ'd in Atlanta.")
with col_arr1:
    st.markdown("##### →")
with col_b:
    with st.container(border=True):
        st.caption("DEPLOYMENT CHANNEL")
        st.markdown("**Scaffold / Access Contractor**")
        st.write("BrandSafway (Alpharetta, GA HQ) · Apache Industrial Services")
        st.caption("Physically deploys LIFTBOT on site under long-term service agreements with owners.")
with col_arr2:
    st.markdown("##### →")
with col_c:
    with st.container(border=True):
        st.caption("AT TAR EXECUTION")
        st.markdown("**LIFTBOT Deployed**")
        st.write("Material handling on scaffolding-heavy maintenance shutdowns")
        st.caption("Owner mandates create pull; contractor labor shortage creates push.")

st.caption(
    "**On channel tension:** Scaffold contractors bill by man-hour, so a labor-cutting "
    "robot can look like a margin threat. This resolves through two forces: (1) a "
    "structural labor shortage — they can't staff large TARs fully anyway — and (2) "
    "owner spec-in mandates, which reframe the contractor as a delivery channel, not a "
    "gatekeeper. BrandSafway's Alpharetta HQ makes them the natural first partnership "
    "conversation in Georgia."
)

# ── MAP ─────────────────────────────────────────────────────────────────────
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

# ── TARGET BREAKDOWN ────────────────────────────────────────────────────────
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

# ── GTM ENTRY SEQUENCE ──────────────────────────────────────────────────────
st.header("GTM Entry Sequence")
st.markdown("A sequenced entry, not a spray. Each step unlocks the next.")

steps = [
    ("Step 1", "BrandSafway Conversation — Alpharetta HQ",
     "BrandSafway is the dominant US scaffold-access contractor and is HQ'd 20 miles from Atlanta. "
     "They operate under long-term service agreements at GP Brunswick, Plant Vogtle, Plant Hatch, and "
     "likely Plant Scherer/Bowen. A partnership conversation here is simultaneously a channel play and "
     "an intelligence source — they know every upcoming TAR in Georgia. This is the first call."),
    ("Step 2", "Georgia-Pacific Brunswick Cellulose Mill — Proof-of-Concept Site",
     "Highest-confidence Tier 1 target. Annual April outage confirmed (Pulp and Paper Chronicle, April "
     "2026), ~1,000 external contractors mobilized. GP is Atlanta-HQ'd (Koch Industries). A successful "
     "LIFTBOT deployment at Brunswick is the reference case that opens every other pulp & paper and "
     "power conversation in the state."),
    ("Step 3", "Southern Company / Georgia Power — Owner-Level Standardization",
     "Southern Company is Atlanta-HQ'd and operates Plant Vogtle (4 nuclear units, near-continuous "
     "outage calendar), Plant Hatch (18-month alternating cycle), Plant Scherer, Plant Bowen, and Plant "
     "Wansley. A spec-in at the Southern Company level means LIFTBOT becomes part of the standard "
     "vendor list for every Georgia Power TAR. Chevron Technology Ventures' strategic investment in "
     "KEWAZO supports owner-level adoption conversations."),
    ("Step 4", "Clearwater Paper Augusta — Pulp & Paper Second Reference",
     "3 confirmed major maintenance outages in 2025, ~$50M total direct cost (Business Wire, Q4 2025 "
     "earnings). Owner is Clearwater Paper (Spokane HQ — remote, but the Augusta mill operates as a "
     "standalone unit). Second reference case for the pulp & paper vertical, demonstrates the pattern "
     "holds beyond GP."),
    ("Step 5", "Expand Across the Southern Company Fleet",
     "With a BrandSafway partnership active and an owner-level relationship at Southern Company, each "
     "Plant Scherer and Plant Bowen outage becomes a repeatable deployment. Plant Bowen's 4 units run "
     "through ~2038 per the 2025 IRP — maximum remaining scaffolding runway in the Georgia power fleet."),
]

for num, title, body in steps:
    with st.container(border=True):
        st.caption(num)
        st.markdown(f"**{title}**")
        st.write(body)
