import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="KEWAZO | Georgia GTM",
    page_icon="🏗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
/* Typography */
h1, h2, h3 { font-family: 'Georgia', serif; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 1100px; }

/* Section headers */
.section-header {
    font-size: 1.65rem; font-weight: 700; color: #0a1628;
    border-bottom: 3px solid #dc3545; padding-bottom: 0.4rem;
    margin: 2.5rem 0 1rem 0;
}

/* Hero */
.hero-title {
    font-size: 2.6rem; font-weight: 700; color: #0a1628; line-height: 1.15;
    margin-bottom: 0.4rem;
}
.hero-sub {
    font-size: 1.1rem; color: #5a6475; margin-bottom: 1.5rem;
}

/* Thesis / callout boxes */
.thesis-box {
    background: #f0f5ff; border-left: 4px solid #0066cc;
    padding: 1.2rem 1.5rem; border-radius: 0 8px 8px 0; margin: 0.8rem 0;
}
.thesis-label {
    font-size: 0.72rem; font-weight: 700; color: #0066cc;
    text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.3rem;
}

/* Stats */
.stat-block { text-align: center; padding: 0.5rem; }
.stat-num { font-size: 2.4rem; font-weight: 700; color: #0a1628; line-height: 1; }
.stat-lbl { font-size: 0.8rem; color: #6c757d; text-transform: uppercase; letter-spacing: 0.06em; margin-top: 0.2rem; }

/* Channel flow */
.flow-box {
    background: #f8f9fa; border: 1px solid #dee2e6;
    padding: 1rem 1.5rem; border-radius: 8px; text-align: center;
    font-weight: 600; color: #0a1628;
}
.flow-arrow { text-align: center; font-size: 1.4rem; color: #dc3545; padding: 0.3rem 0; }

/* GTM steps */
.gtm-step {
    background: #fff; border: 1px solid #e0e0e0;
    border-left: 4px solid #dc3545; padding: 0.9rem 1.2rem;
    border-radius: 0 8px 8px 0; margin-bottom: 0.7rem;
}
.step-num { font-size: 0.7rem; font-weight: 700; color: #dc3545; text-transform: uppercase; }

/* Automation */
.auto-step {
    background: #f8f9fa; border: 1px solid #dee2e6;
    padding: 0.8rem 1.2rem; border-radius: 8px; margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

/* Map legend */
.legend-item { display: flex; align-items: center; gap: 8px; margin: 4px 0; font-size: 0.85rem; }
.legend-dot { width: 14px; height: 14px; border-radius: 50%; flex-shrink: 0; }

/* Methodology */
.method-card {
    background: #f8f9fa; border: 1px solid #dee2e6;
    padding: 1rem 1.2rem; border-radius: 8px; margin-bottom: 0.6rem;
}
.method-label { font-size: 0.7rem; font-weight: 700; color: #6c757d; text-transform: uppercase; letter-spacing: 0.06em; }
</style>
""", unsafe_allow_html=True)


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
st.markdown('<div class="hero-title">Georgia: KEWAZO\'s Next US Industrial Market</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">A targeted GTM thesis &nbsp;·&nbsp; Lorenzo Leprotti &nbsp;·&nbsp; June 2026</div>', unsafe_allow_html=True)
st.divider()

# ── THESIS ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">The Thesis</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class='thesis-box'>
    <div class='thesis-label'>Part 1 — The Base</div>
    <b>Georgia's process-industry base drives recurring revenue.</b> Pulp &amp; paper mills and power plants run scheduled maintenance turnarounds on annual to 18-month cycles. This is exactly KEWAZO's proven use case — the same job shape as Gulf Coast energy work. Atlanta-headquartered owners (Georgia Power, Georgia-Pacific) control both sides of the spec-in decision.
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='thesis-box'>
    <div class='thesis-label'>Part 2 — The Timing Wedge</div>
    <b>A $20B+ manufacturing boom creates urgency now.</b> Hyundai Metaplant, battery plants, Qcells, Rivian — active megaproject construction means scaffolding-heavy builds today. This is the "why now," not the core thesis. It opens the door; the turnaround base keeps it open.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("8", "Tier 1 beachhead targets"),
    ("~Annual", "Avg TAR cadence, top sites"),
    ("15–25%", "Scaffolding share of TAR labor"),
    ("~70%", "LIFTBOT material-handling reduction"),
]
for col, (num, lbl) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""
        <div class='stat-block'>
        <div class='stat-num'>{num}</div>
        <div class='stat-lbl'>{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style='background:#fff5f5; border:1px solid #f5c6cb; border-radius:8px; padding:0.9rem 1.2rem; margin-top:1.2rem; font-size:0.9rem'>
<b>The value anchor:</b> Scaffolding is ~15–25% of total turnaround direct labor (up to 35–40% when access is reactive).
A ~70% reduction in scaffold material-handling translates to roughly <b>10–17% reduction in total TAR direct labor cost</b> — a board-level number for asset owners running multi-million-dollar outages.
</div>
""", unsafe_allow_html=True)

# ── BUYER MODEL ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">The Buyer Model</div>', unsafe_allow_html=True)

st.markdown("""
Georgia is unusual: <b>both ends of the GTM sit in metro Atlanta.</b>
Asset owners who approve the technology and scaffold contractors who deploy it on site are both headquartered here.
""", unsafe_allow_html=True)

col_a, col_arr1, col_b, col_arr2, col_c = st.columns([3, 0.5, 3, 0.5, 3])
with col_a:
    st.markdown("""
    <div class='flow-box' style='border-top:4px solid #dc3545'>
    <div style='font-size:0.7rem;color:#dc3545;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem'>Decision-Maker</div>
    <b>Asset Owner / Operator</b><br>
    <span style='font-size:0.85rem;color:#5a6475'>Georgia Power · Southern Company<br>Georgia-Pacific · Clearwater Paper</span><br><br>
    <span style='font-size:0.8rem'>Specs-in LIFTBOT, sets the TAR plan, approves vendors. HQ'd in Atlanta.</span>
    </div>
    """, unsafe_allow_html=True)
with col_arr1:
    st.markdown("<div class='flow-arrow' style='padding-top:2.5rem'>→</div>", unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class='flow-box' style='border-top:4px solid #fd7e14'>
    <div style='font-size:0.7rem;color:#fd7e14;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem'>Deployment Channel</div>
    <b>Scaffold / Access Contractor</b><br>
    <span style='font-size:0.85rem;color:#5a6475'>BrandSafway (Alpharetta, GA HQ)<br>Apache Industrial Services</span><br><br>
    <span style='font-size:0.8rem'>Physically deploys LIFTBOT on site under long-term service agreements with owners.</span>
    </div>
    """, unsafe_allow_html=True)
with col_arr2:
    st.markdown("<div class='flow-arrow' style='padding-top:2.5rem'>→</div>", unsafe_allow_html=True)
with col_c:
    st.markdown("""
    <div class='flow-box' style='border-top:4px solid #0066cc'>
    <div style='font-size:0.7rem;color:#0066cc;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem'>At TAR Execution</div>
    <b>LIFTBOT Deployed</b><br>
    <span style='font-size:0.85rem;color:#5a6475'>Material handling on scaffolding-heavy maintenance shutdowns</span><br><br>
    <span style='font-size:0.8rem'>Owner mandates create pull; contractor labor shortage creates push.</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='background:#f8f9fa; border:1px solid #dee2e6; border-radius:8px; padding:0.9rem 1.2rem; margin-top:1rem; font-size:0.85rem; color:#5a6475'>
<b>On channel tension:</b> Scaffold contractors bill by man-hour, so a labor-cutting robot can look like a margin threat.
This resolves through two forces: (1) a structural labor shortage — they can't staff large TARs fully anyway —
and (2) owner spec-in mandates, which reframe the contractor as a delivery channel, not a gatekeeper.
BrandSafway's Alpharetta HQ makes them the natural first partnership conversation in Georgia.
</div>
""", unsafe_allow_html=True)

# ── MAP ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">Target Map — Georgia Industrial Sites</div>', unsafe_allow_html=True)

col_legend, col_map = st.columns([1, 5])
with col_legend:
    st.markdown("""
    <div style='padding-top:1rem'>
    <div style='font-size:0.78rem; font-weight:700; color:#6c757d; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.6rem'>Tier Legend</div>
    <div class='legend-item'><div class='legend-dot' style='background:#dc3545'></div><b>Tier 1</b> — Beachhead<br><span style='font-size:0.75rem;color:#6c757d'>Recurring process TARs</span></div>
    <div class='legend-item' style='margin-top:8px'><div class='legend-dot' style='background:#fd7e14'></div><b>Tier 2</b> — Timing Wedge<br><span style='font-size:0.75rem;color:#6c757d'>Active megaproject builds</span></div>
    <div class='legend-item' style='margin-top:8px'><div class='legend-dot' style='background:#6c757d'></div><b>Tier 3</b> — Adjacent<br><span style='font-size:0.75rem;color:#6c757d'>Expansion optionality</span></div>
    <div style='margin-top:1.5rem; font-size:0.75rem; color:#9ca3af'>Hover pins for detail</div>
    </div>
    """, unsafe_allow_html=True)

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
st.markdown('<div class="section-header">Target Breakdown &amp; ICP Scoring</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section-header">GTM Entry Sequence</div>', unsafe_allow_html=True)

st.markdown("A sequenced entry, not a spray. Each step unlocks the next.")
st.markdown("<br>", unsafe_allow_html=True)

steps = [
    ("Step 1", "BrandSafway Conversation — Alpharetta HQ",
     "BrandSafway is the dominant US scaffold-access contractor and is HQ'd 20 miles from Atlanta. They operate under long-term service agreements at GP Brunswick, Plant Vogtle, Plant Hatch, and likely Plant Scherer/Bowen. A partnership conversation here is simultaneously a channel play and an intelligence source — they know every upcoming TAR in Georgia. This is the first call."),
    ("Step 2", "Georgia-Pacific Brunswick Cellulose Mill — Proof-of-Concept Site",
     "Highest-confidence Tier 1 target. Annual April outage confirmed (Pulp and Paper Chronicle, April 2026), ~1,000 external contractors mobilized. GP is Atlanta-HQ'd (Koch Industries). A successful LIFTBOT deployment at Brunswick is the reference case that opens every other pulp &amp; paper and power conversation in the state."),
    ("Step 3", "Southern Company / Georgia Power — Owner-Level Standardization",
     "Southern Company is Atlanta-HQ'd and operates Plant Vogtle (4 nuclear units, near-continuous outage calendar), Plant Hatch (18-month alternating cycle), Plant Scherer, Plant Bowen, and Plant Wansley. A spec-in at the Southern Company level means LIFTBOT becomes part of the standard vendor list for every Georgia Power TAR. Chevron Technology Ventures' strategic investment in KEWAZO supports owner-level adoption conversations."),
    ("Step 4", "Clearwater Paper Augusta — Pulp &amp; Paper Second Reference",
     "3 confirmed major maintenance outages in 2025, ~$50M total direct cost (Business Wire, Q4 2025 earnings). Owner is Clearwater Paper (Spokane HQ — remote, but the Augusta mill operates as a standalone unit). Second reference case for the pulp &amp; paper vertical, demonstrates the pattern holds beyond GP."),
    ("Step 5", "Expand Across the Southern Company Fleet",
     "With a BrandSafway partnership active and an owner-level relationship at Southern Company, each Plant Scherer and Plant Bowen outage becomes a repeatable deployment. Plant Bowen's 4 units run through ~2038 per the 2025 IRP — maximum remaining scaffolding runway in the Georgia power fleet."),
]

for num, title, body in steps:
    st.markdown(f"""
    <div class='gtm-step'>
    <div class='step-num'>{num}</div>
    <b>{title}</b><br>
    <span style='font-size:0.88rem; color:#5a6475; line-height:1.6'>{body}</span>
    </div>
    """, unsafe_allow_html=True)

# ── AUTOMATION SUBSECTION ───────────────────────────────────────────────────
st.markdown('<div class="section-header">Hypothetical Execution Flow</div>', unsafe_allow_html=True)

st.markdown("""
The GTM motion is sequenced, not automated — but the execution layer is tool-agnostic.
Below is a hypothetical workflow showing how Lorenzo would instrument the outreach and follow-up cycle.
<b>This is a delivery assumption, not a KEWAZO system.</b> Swapping Make for n8n (or the reverse) is a configuration change, not a strategy change.
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
flow_steps = [
    ("Trigger", "TAR schedule alert", "Monitor trade press (Pulp &amp; Paper Chronicle, Fastmarkets, Global Energy Monitor) for announced outage windows. Trigger: new TAR date confirmed at a Tier 1 site."),
    ("Enrich", "Site + owner lookup", "Pull owner contact, recent TAR history, and BrandSafway contract status from internal CRM. Flag if BrandSafway is the incumbent contractor."),
    ("Route", "Dual-track outreach", "Route to (A) owner-level KEWAZO account team for spec-in conversation and (B) BrandSafway regional manager for deployment coordination."),
    ("Track", "Pipeline entry + follow-up", "Log TAR date, site, and outreach status. Auto-reminder 90 days before outage window for pre-mobilization check-in."),
    ("Capture", "Post-deployment data", "After deployment: log LIFTBOT hours, scaffold-hours avoided, crew headcount. Feed back to KEWAZO's ROI documentation."),
]
for trigger, label, desc in flow_steps:
    st.markdown(f"""
    <div class='auto-step'>
    <span style='font-size:0.7rem;font-weight:700;color:#6c757d;text-transform:uppercase;letter-spacing:0.06em'>{trigger}</span>
    <b style='margin:0 0.5rem'>{label}</b>
    <span style='font-size:0.85rem;color:#5a6475'>{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='font-size:0.8rem; color:#9ca3af; margin-top:0.5rem'>
Tool stack assumption: Make (or n8n) for orchestration &nbsp;·&nbsp; HubSpot / Pipedrive for CRM &nbsp;·&nbsp; Notion for TAR calendar tracking.
None of this requires custom software — it's a configured workflow, deployable in a week.
</div>
""", unsafe_allow_html=True)

# ── METHODOLOGY ─────────────────────────────────────────────────────────────
st.divider()
st.markdown('<div class="section-header">How This Was Built</div>', unsafe_allow_html=True)

st.markdown("A short account of the method. The point is not the conclusion alone, but that it was reached in a structured, verifiable way.")
st.markdown("<br>", unsafe_allow_html=True)

method_items = [
    ("The question", "Could Georgia be KEWAZO's next US industrial market, and which sites would you target first? Scope deliberately bounded: scaffolding-intensive maintenance turnarounds in process industries as the beachhead, construction boom as the timing wedge."),
    ("Spec before build", "Started with a PRD, not code. Defined purpose, audience, scope, and explicit out-of-scope before anything was built. Strategy drives the artifact, not the other way around."),
    ("Verification", "Every factual claim verified with source + date. Rules: no source → no row. Closed mills removed. Rounded coordinates corrected against authoritative sources (Global Energy Monitor, Wikipedia infobox, official addresses). Confidence flagged per row. Weak citations upgraded (GP Brunswick moved from county Facebook post to Pulp and Paper Chronicle trade press)."),
    ("The buyer model", "Held as an explicit assumption, then tested. Research confirmed: dual buyer (owner specs-in, contractor deploys), two contracting structures (direct and through turnaround management contractor), with BrandSafway as the dominant Georgia-market channel. Value quantified: 15–25% of TAR labor is scaffolding; LIFTBOT's ~70% material-handling reduction → 10–17% total TAR labor cost reduction."),
    ("Tools", "Reasoning and PRD: Claude. Fact verification: Perplexity (deep research). Data: portable CSV, one row per site, decoupled from code. Delivery: Streamlit + pydeck."),
    ("Honest boundaries", "The buyer model is research-confirmed for the sector, not validated inside KEWAZO. GP Rincon TAR cadence has no confirmed public schedule (confidence: medium). Tier 3 sites are completeness, not live targets. These are flagged rather than hidden."),
]

for label, body in method_items:
    st.markdown(f"""
    <div class='method-card'>
    <div class='method-label'>{label}</div>
    <div style='font-size:0.9rem; color:#1a1a2e; margin-top:0.3rem; line-height:1.6'>{body}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; color:#9ca3af; font-size:0.8rem; margin-top:2rem; padding-top:1rem; border-top:1px solid #dee2e6'>
Lorenzo Leprotti &nbsp;·&nbsp; June 2026 &nbsp;·&nbsp; All data sourced and verified &nbsp;·&nbsp; Built with Streamlit + pydeck
</div>
""", unsafe_allow_html=True)
