import streamlit as st
import pandas as pd

st.title("Georgia GTM Strategy")
st.caption("Why Georgia, why now, and how KEWAZO gets in · Lorenzo Leprotti · June 2026")
st.divider()

# ── THE PROBLEM ──────────────────────────────────────────────────────────────
st.header("The Problem")

st.write(
    "Large process-industry facilities (paper mills, nuclear plants, fossil fuel power plants) "
    "run scheduled maintenance shutdowns where all non-essential equipment is taken offline for "
    "inspection, repair, and replacement. During these shutdowns, scaffolding goes up around "
    "boilers, turbines, pressure vessels, and other machinery. Erecting, stocking, and "
    "dismantling that scaffolding is the most labor-intensive and one of the most dangerous "
    "parts of the shutdown."
)

st.write(
    "Scaffolding accounts for 15 to 25 percent of total direct labor on a maintenance shutdown, "
    "rising to 35 to 40 percent when access is planned reactively. Contractors already struggle "
    "to staff these jobs: skilled scaffolding crews are in short supply, and large shutdowns "
    "require hundreds of workers simultaneously. The material-handling portion of that work, "
    "moving loads up and through the structure, is done almost entirely by hand."
)

st.write(
    "LIFTBOT automates that material-handling step. KEWAZO's documented range is a "
    "40 to 70 percent reduction in material-handling labor, with industrial deployments "
    "typically closer to 40 percent. On a shutdown where scaffolding is 20 percent of "
    "total direct labor, that translates to an 8 to 14 percent reduction in total "
    "shutdown direct labor cost."
)

st.divider()

# ── MARKET SIZING ────────────────────────────────────────────────────────────
st.header("Georgia's Industrial Maintenance Market")

st.write(
    "The analysis identified eight process-industry facilities in Georgia that run "
    "scaffolding-intensive maintenance shutdowns on recurring cycles. The market sizing "
    "below is built bottom-up from those sites using documented shutdown data where "
    "available and published industry benchmarks where not."
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Priority facilities (T1)", "8")
c2.metric("Est. aggregate shutdown labor", "~$164M / yr", help="Bottom-up from 8 T1 sites. Clearwater Augusta confirmed ($16M, Q3 2025 earnings); nuclear per NEI/Industrial Info Resources benchmarks; coal/gas estimated. Treat as indicative.")
c3.metric("Scaffolding share of shutdown labor", "15-25%", help="AMECO (2023): 20% of total direct field labor. BrandSafway / Hydrocarbon Engineering: 15-25%, up to 35-40% when access is reactive.")
c4.metric("LIFTBOT material-handling reduction", "40-70%")

st.info(
    "**Market anchor: Clearwater Paper Augusta Mill.** Three confirmed major maintenance "
    "outages across Clearwater's three mills in 2025, approximately \\$50M combined in "
    "direct labor. The Augusta mill alone accounts for roughly \\$16M (confirmed, Q3 2025 "
    "earnings call). At 20 percent scaffolding share, that is approximately \\$3M in "
    "scaffolding labor at Augusta in a single year."
)

sizing_df = pd.DataFrame([
    {"Site": "Clearwater Paper Augusta", "Est. annual outage cost": "~$16M (confirmed, Clearwater IR Q3 2025)", "Scaffolding share (20%)": "~$3.2M"},
    {"Site": "GP Brunswick Cellulose", "Est. annual outage cost": "~$10-15M (estimated; no public figure)", "Scaffolding share (20%)": "~$2-3M"},
    {"Site": "GP Rincon", "Est. annual outage cost": "~$8-12M (estimated, tissue mill)", "Scaffolding share (20%)": "~$1.6-2.4M"},
    {"Site": "Plant Vogtle (4 units, staggered ~18 mo)", "Est. annual outage cost": "~$53M / yr equiv. (~$20M/unit × 4 ÷ 1.5)", "Scaffolding share (20%)": "~$10.6M"},
    {"Site": "Plant Hatch (2 units, ~18 mo)", "Est. annual outage cost": "~$24M / yr equiv. (~$18M/unit × 2 ÷ 1.5)", "Scaffolding share (20%)": "~$4.8M"},
    {"Site": "Plant Bowen (4 units, every 3 yr)", "Est. annual outage cost": "~$20M / yr equiv. (~$15M/unit × 4 ÷ 3)", "Scaffolding share (20%)": "~$4M"},
    {"Site": "Plant Scherer (3 units, every 3 yr)", "Est. annual outage cost": "~$15M / yr equiv. (~$15M/unit × 3 ÷ 3)", "Scaffolding share (20%)": "~$3M"},
    {"Site": "Plant Wansley (gas CC, every 4 yr)", "Est. annual outage cost": "~$8M / yr equiv. (~$8M/unit × 4 ÷ 4)", "Scaffolding share (20%)": "~$1.6M"},
    {"Site": "Total", "Est. annual outage cost": "~$164M / yr", "Scaffolding share (20%)": "~$33M / yr"},
])
st.dataframe(sizing_df, use_container_width=True, hide_index=True)

st.write(
    "Of the approximately \\$33M in annual scaffolding labor across T1 sites, LIFTBOT's "
    "40 to 70 percent reduction on material handling represents \\$13M to \\$23M in annual "
    "savings available to Georgia T1 owners. Nuclear plant outages (Vogtle, Hatch) carry "
    "roughly half that opportunity given their scale and frequency."
)

st.caption(
    "Three large Georgia paper mills closed in summer 2025: GP Cedar Springs (August 2025), "
    "IP Savannah, and IP Riceboro (September 2025). The active kraft and tissue mill count "
    "dropped from six to three. The surviving mills (GP Brunswick, GP Rincon, Clearwater Augusta) "
    "are larger and better-capitalized. The \\$164M estimate reflects the post-closure T1 set."
)

st.divider()

# ── WHY GEORGIA ──────────────────────────────────────────────────────────────
st.header("Why Georgia")

st.markdown(
    "- **Right facility type.** Georgia's industrial base is dominated by process industries: "
    "pulp and paper, power generation, chemicals. These are the only sectors where "
    "scaffolding-intensive recurring maintenance shutdowns are standard practice. "
    "Discrete manufacturing (auto assembly, electronics) does not generate comparable demand.\n\n"
    "- **Both buyers are in Atlanta.** Georgia Power and Georgia-Pacific, the two largest asset "
    "owners in the T1 pipeline, are headquartered in Atlanta. BrandSafway, the dominant "
    "scaffolding contractor in the Southeast, is also headquartered in Atlanta (600 Galleria "
    "Pkwy SE). Both sides of every LIFTBOT sale are reachable from one city.\n\n"
    "- **A construction boom opens doors now.** A \\$20B+ manufacturing build-out is underway: "
    "Hyundai Metaplant, Qcells solar, multiple battery plants, Rivian. These sites generate "
    "scaffolding demand today and put KEWAZO in front of contractors and owners actively "
    "deploying crews at scale right now.\n\n"
    "- **Small, reachable target set.** Eight priority facilities. Two owner companies "
    "(Georgia Power and Georgia-Pacific together own six of the eight). One dominant "
    "contractor (BrandSafway). A focused enterprise sales effort can cover this "
    "systematically without spray-and-pray."
)

st.divider()

# ── FIRST MOVE ───────────────────────────────────────────────────────────────
st.header("The First Move")

st.write(
    "Identifying a target market is not a go-to-market strategy. This section makes it "
    "concrete: which site to approach first, who to reach, how to get there, and what "
    "events put KEWAZO in the same room as the right people."
)

with st.container(border=True):
    st.markdown("**Top priority target: Georgia-Pacific Brunswick Cellulose Mill**")
    col_a, col_b = st.columns(2)
    with col_a:
        st.caption("WHY THIS SITE FIRST")
        st.write(
            "Confirmed annual April shutdown with a secondary October window. "
            "951,000 tonnes per year capacity, 600+ employees, one of the largest "
            "single-product pulp mills in North America. The shutdown cadence is "
            "public and predictable, which means KEWAZO can time outreach to arrive "
            "months before the next outage, not after it has already been staffed."
        )
    with col_b:
        st.caption("OWNERSHIP ADVANTAGE")
        st.write(
            "Georgia-Pacific is headquartered in Atlanta (Koch Industries subsidiary). "
            "A vendor relationship approved at the corporate level applies across all "
            "GP mills in the state, including the Rincon mill. Winning one site through "
            "corporate approval is a faster path to two sites than selling each "
            "independently."
        )

st.subheader("Who to Reach")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.caption("SITE LEVEL")
        st.markdown("**Maintenance Manager, GP Brunswick**")
        st.write(
            "Controls the shutdown plan and day-to-day contractor relationships "
            "on site. Has the direct pain. First conversation is about April "
            "shutdown logistics and scaffolding crew availability problems."
        )

with col2:
    with st.container(border=True):
        st.caption("CORPORATE LEVEL")
        st.markdown("**VP Manufacturing Operations, Georgia-Pacific (Atlanta)**")
        st.write(
            "Sets vendor policy across all GP mills. A pilot approval at this "
            "level unlocks all sites, not just Brunswick. Target after the "
            "site-level relationship is established."
        )

with col3:
    with st.container(border=True):
        st.caption("DEPLOYMENT CHANNEL")
        st.markdown("**VP Operations, BrandSafway (Atlanta HQ)**")
        st.write(
            "BrandSafway likely holds the GP Brunswick scaffold contract "
            "(commercially inferred from their sector positioning and Georgia "
            "footprint; no contract is publicly confirmed). Getting to them first "
            "is a shortcut: one relationship unlocks every site they service in Georgia."
        )

st.subheader("How to Get There")

st.markdown(
    "**Path 1: Contractor first (fastest).** BrandSafway's Atlanta office is the highest-leverage "
    "first call. If they hold the GP Brunswick contract and agree to pilot LIFTBOT, they "
    "facilitate the owner introduction and handle on-site deployment. One relationship "
    "unlocks multiple sites.\n\n"
    "**Path 2: Owner direct.** Georgia-Pacific corporate is in Atlanta. Outreach to their "
    "VP of Manufacturing Operations, citing the specific Brunswick April shutdown and the "
    "Clearwater Augusta \\$50M benchmark, makes the pitch concrete rather than generic.\n\n"
    "**Path 3: Conference.** Both paths benefit from meeting targets at industry events "
    "before the cold call. The table below shows where the right people actually show up."
)

events_df = pd.DataFrame([
    {
        "Event": "TAPPI PaperCon",
        "Who attends": "Maintenance managers and operations VPs at pulp & paper mills",
        "Relevance": "Direct access to GP Brunswick and Clearwater Augusta decision-makers. Annual, April/May.",
    },
    {
        "Event": "SAIA Annual Convention",
        "Who attends": "Scaffold and access industry executives including BrandSafway leadership",
        "Relevance": "BrandSafway is a major SAIA member. The contractor relationship starts here.",
    },
    {
        "Event": "SMRP Annual Conference",
        "Who attends": "Maintenance and reliability engineers across all process industries",
        "Relevance": "Plant-level maintenance managers from paper, power, chemical. Broadest T1 buyer coverage.",
    },
    {
        "Event": "POWERGEN International",
        "Who attends": "Power generation operations and maintenance teams",
        "Relevance": "Georgia Power and Southern Company attend. Entry point for the four T1 power plants.",
    },
    {
        "Event": "Nuclear Energy Assembly (NEI)",
        "Who attends": "Nuclear plant operators including Southern Nuclear",
        "Relevance": "Vogtle and Hatch contacts. Nuclear outages carry the largest single shutdown budgets in the T1 set.",
    },
])
st.dataframe(events_df, use_container_width=True, hide_index=True)

st.divider()

# ── BUYER MODEL ──────────────────────────────────────────────────────────────
st.header("The Buyer Model")

st.write(
    "There are two decision-makers in every LIFTBOT deployment. The asset owner approves "
    "the technology and specifies it into the shutdown plan. The scaffolding contractor "
    "physically deploys it on site. Both need to be sold, in that order."
)

col_1, col_arr1, col_2, col_arr2, col_3 = st.columns([3, 0.5, 3, 0.5, 3])

with col_1:
    with st.container(border=True):
        st.caption("STEP 1: SPECIFICATION")
        st.markdown("**Asset Owner / Operator**")
        st.write("Georgia Power · Southern Company · Georgia-Pacific · Clearwater Paper")
        st.caption(
            "Approves LIFTBOT, sets the shutdown plan, mandates vendor. "
            "All major T1 owners are headquartered in Atlanta."
        )

with col_arr1:
    st.markdown("##### →")

with col_2:
    with st.container(border=True):
        st.caption("STEP 2: DEPLOYMENT")
        st.markdown("**Scaffold Contractor**")
        st.write("BrandSafway (Atlanta HQ) · Apache Industrial Services")
        st.caption(
            "Physically deploys LIFTBOT on site under long-term service "
            "agreements with asset owners."
        )

with col_arr2:
    st.markdown("##### →")

with col_3:
    with st.container(border=True):
        st.caption("OUTCOME")
        st.markdown("**Shutdown Executed with LIFTBOT**")
        st.write("Material handling automated; smaller crew, faster cycle, fewer injuries")
        st.caption(
            "Owner captures the cost reduction. Contractor captures the labor "
            "shortage buffer: they can execute larger shutdowns with fewer bodies."
        )

st.caption(
    "**On channel tension:** Scaffold contractors bill by man-hour, so a labor-saving robot "
    "looks like a margin threat. Two forces soften this: a structural skilled-labor shortage "
    "means contractors cannot fully staff large shutdowns anyway, and owner mandates reframe "
    "the contractor as a delivery channel rather than a gatekeeper. The harder constraint is "
    "timing: owners write LIFTBOT into the shutdown specification 12 to 18 months before the "
    "outage, during annual maintenance planning. KEWAZO must get into the owner's planning "
    "cycle before the contractor is even engaged. A documented pilot result from one Clearwater "
    "or GP mill is what gets LIFTBOT into subsequent shutdown specifications across the "
    "portfolio. BrandSafway's Atlanta headquarters makes them the natural first conversation."
)
