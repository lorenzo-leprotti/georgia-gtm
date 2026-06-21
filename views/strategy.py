import streamlit as st

st.title("Georgia GTM Strategy")
st.caption("Why Georgia, why now, and how KEWAZO gets in · Lorenzo Leprotti · June 2026")
st.divider()

# ── THE PROBLEM ──────────────────────────────────────────────────────────────
st.header("The Problem")

st.write(
    "Large process-industry facilities — paper mills, nuclear plants, fossil fuel "
    "power plants — run scheduled maintenance shutdowns where all non-essential "
    "equipment is taken offline for inspection, repair, and replacement. During these "
    "shutdowns, scaffolding goes up around boilers, turbines, pressure vessels, and "
    "other machinery. Erecting, stocking, and dismantling that scaffolding is the "
    "most labor-intensive and one of the most dangerous parts of the shutdown."
)

st.write(
    "Scaffolding accounts for 15 to 25 percent of total direct labor on a "
    "maintenance shutdown — rising to 35 to 40 percent when access is planned "
    "reactively. Contractors already struggle to staff these jobs: skilled scaffolding "
    "crews are in short supply, and large shutdowns require hundreds of workers "
    "simultaneously. The material-handling portion of that work — moving loads "
    "up and through the structure — is done almost entirely by hand."
)

st.write(
    "LIFTBOT automates that material-handling step. KEWAZO's documented result is a "
    "~70 percent reduction in the material-handling labor requirement. On a shutdown "
    "where scaffolding is 20 percent of total direct labor, that translates to a "
    "10 to 14 percent reduction in total shutdown direct labor cost."
)

st.divider()

# ── MARKET SIZING ────────────────────────────────────────────────────────────
st.header("Georgia's Industrial Maintenance Market")

st.write(
    "The analysis identified eight process-industry facilities in Georgia that run "
    "scaffolding-intensive maintenance shutdowns on recurring cycles. These are the "
    "priority targets. The market sizing below is built bottom-up from those sites "
    "using documented shutdown data where available and published industry benchmarks "
    "where not."
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Priority facilities (T1)", "8")
c2.metric("Est. aggregate shutdown labor", ">$350M / yr", help="Bottom-up estimate across 8 T1 sites. See methodology for sources.")
c3.metric("Scaffolding share of shutdown labor", "15–25%")
c4.metric("LIFTBOT material-handling reduction", "~70%")

st.info(
    "**Market anchor — Clearwater Paper Augusta Mill:** Three confirmed major "
    "maintenance outages in 2025, approximately \\$50M in total direct labor. "
    "At 20 percent scaffolding share, that is ~\\$10M in scaffolding labor at one "
    "mid-sized paper mill in a single year. The eight T1 sites include two larger "
    "Georgia-Pacific mills and four multi-unit power plants with comparable or "
    "larger shutdown budgets."
)

st.write(
    "The \\$350M figure is a conservative floor: it does not include the six Tier 2 "
    "construction sites, which represent additional near-term scaffolding demand "
    "during the build phase. Plant Vogtle alone — the largest nuclear facility in "
    "the US — runs near-continuous outages across four units, with each refueling "
    "outage carrying an estimated \\$50M to \\$150M in direct labor."
)

st.divider()

# ── WHY GEORGIA ──────────────────────────────────────────────────────────────
st.header("Why Georgia")

col_a, col_b = st.columns(2)

with col_a:
    with st.container(border=True):
        st.markdown("**The right type of facilities**")
        st.write(
            "Georgia's industrial base is heavily weighted toward process "
            "industries — paper, power, chemicals — where scaffolding-intensive "
            "maintenance shutdowns are routine and recurring. This is different "
            "from discrete manufacturing (auto assembly, electronics), where "
            "maintenance is more contained and scaffolding demand is limited."
        )

with col_b:
    with st.container(border=True):
        st.markdown("**Both buyers are local**")
        st.write(
            "Georgia is unusual: both sides of the commercial relationship are "
            "headquartered in metro Atlanta. Georgia Power and Georgia-Pacific — "
            "the two largest asset owners in the T1 pipeline — are Atlanta-based. "
            "BrandSafway, the dominant scaffolding contractor in the Southeast and "
            "a likely deployment channel for LIFTBOT, is headquartered in Alpharetta. "
            "This compresses the cost of building both relationships simultaneously."
        )

col_c, col_d = st.columns(2)

with col_c:
    with st.container(border=True):
        st.markdown("**A construction boom creates near-term demand**")
        st.write(
            "A $20B+ manufacturing build-out — Hyundai Metaplant, multiple battery "
            "plants, Qcells solar, Rivian — means scaffolding-heavy construction "
            "is happening in Georgia right now. These sites do not generate recurring "
            "maintenance shutdowns, but they open conversations with contractors "
            "and owners who are actively deploying scaffolding crews at scale."
        )

with col_d:
    with st.container(border=True):
        st.markdown("**A defined, reachable set of targets**")
        st.write(
            "Eight priority facilities, two owner companies (Georgia Power and "
            "Georgia-Pacific together own six of the eight), and one dominant "
            "contractor (BrandSafway). This is a narrow enough target set that "
            "a two-person enterprise sales effort can cover it in a structured "
            "account-based motion without spray-and-pray."
        )

st.divider()

# ── BUYER MODEL ──────────────────────────────────────────────────────────────
st.header("The Buyer Model")

st.write(
    "There are two decision-makers in every LIFTBOT deployment. The asset owner "
    "approves the technology and specifies it into the shutdown plan. The scaffolding "
    "contractor physically deploys it on site. Both need to be sold — in that order."
)

col_1, col_arr1, col_2, col_arr2, col_3 = st.columns([3, 0.5, 3, 0.5, 3])

with col_1:
    with st.container(border=True):
        st.caption("STEP 1 — SPECIFICATION")
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
        st.caption("STEP 2 — DEPLOYMENT")
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
            "shortage buffer — they can execute larger shutdowns with fewer bodies."
        )

st.caption(
    "**On channel tension:** Scaffold contractors bill by man-hour, so a "
    "labor-saving robot can look like a margin threat. In practice, two forces "
    "resolve this: a structural skilled-labor shortage means contractors cannot "
    "fully staff large shutdowns anyway, and owner mandates reframe the contractor "
    "as a delivery channel rather than a gatekeeper. BrandSafway's Alpharetta "
    "headquarters makes them the natural first conversation in Georgia."
)
