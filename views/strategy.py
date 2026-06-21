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
    "LIFTBOT automates that material-handling step. KEWAZO's documented result is a "
    "70 percent reduction in the material-handling labor requirement. On a shutdown where "
    "scaffolding is 20 percent of total direct labor, that translates to a 10 to 14 percent "
    "reduction in total shutdown direct labor cost."
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
c2.metric("Est. aggregate shutdown labor", ">$350M / yr", help="Bottom-up estimate across 8 T1 sites. See methodology for sources.")
c3.metric("Scaffolding share of shutdown labor", "15-25%")
c4.metric("LIFTBOT material-handling reduction", "~70%")

st.info(
    "**Market anchor: Clearwater Paper Augusta Mill.** Three confirmed major maintenance "
    "outages in 2025, approximately \\$50M in total direct labor. At 20 percent scaffolding "
    "share, that is roughly \\$10M in scaffolding labor at one mid-sized paper mill in a "
    "single year. The eight T1 sites include two larger Georgia-Pacific mills and four "
    "multi-unit power plants with comparable or larger shutdown budgets."
)

st.write(
    "The \\$350M figure is a conservative floor. It does not include the six Tier 2 "
    "construction sites, which represent additional near-term scaffolding demand during "
    "the build phase. Plant Vogtle alone, the largest nuclear facility in the US, runs "
    "near-continuous outages across four units, with each refueling outage carrying an "
    "estimated \\$50M to \\$150M in direct labor."
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
    "scaffolding contractor in the Southeast, is headquartered in Alpharetta. Both sides of "
    "every LIFTBOT sale are reachable from one city.\n\n"
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
        st.markdown("**VP Operations, BrandSafway (Alpharetta)**")
        st.write(
            "BrandSafway almost certainly holds the GP Brunswick scaffold "
            "contract. Getting to them first is a shortcut: they can introduce "
            "KEWAZO to every site they service in Georgia. 20 minutes from Atlanta."
        )

st.subheader("How to Get There")

st.markdown(
    "**Path 1: Contractor first (fastest).** BrandSafway Alpharetta is the highest-leverage "
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
        st.write("BrandSafway (Alpharetta HQ) · Apache Industrial Services")
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
    "**On channel tension:** Scaffold contractors bill by man-hour, so a labor-saving "
    "robot can look like a margin threat. In practice two forces resolve this: a structural "
    "skilled-labor shortage means contractors cannot fully staff large shutdowns anyway, "
    "and owner mandates reframe the contractor as a delivery channel rather than a gatekeeper. "
    "BrandSafway's Alpharetta headquarters makes them the natural first conversation in Georgia."
)
