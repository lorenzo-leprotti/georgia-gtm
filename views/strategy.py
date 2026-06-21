import streamlit as st

st.title("Georgia: KEWAZO's Next US Industrial Market")
st.caption("A targeted GTM thesis · Lorenzo Leprotti · June 2026")
st.divider()

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
        "**Part 2 — The Construction Boom**\n\n"
        "A $20B+ manufacturing boom creates urgency now. Hyundai Metaplant, battery "
        "plants, Qcells, Rivian — active megaproject construction means scaffolding-heavy "
        "builds today. This is the \"why now,\" not the core thesis. It opens the door; "
        "the recurring maintenance base keeps it open."
    )

c1, c2, c3, c4 = st.columns(4)
stats = [
    ("Priority targets identified", "8"),
    ("Maintenance interval, top sites", "~Annual"),
    ("Scaffolding share of shutdown labor", "15–25%"),
    ("LIFTBOT material-handling reduction", "~70%"),
]
for col, (lbl, num) in zip([c1, c2, c3, c4], stats):
    col.metric(lbl, num)

st.warning(
    "**The value anchor:** Scaffolding is ~15–25% of total shutdown direct labor "
    "(up to 35–40% when access is planned reactively). A ~70% reduction in scaffold "
    "material-handling translates to roughly **10–17% reduction in total shutdown direct "
    "labor cost** — a board-level number for asset owners running multi-million-dollar "
    "outages."
)

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
        st.caption("Specifies LIFTBOT, sets the maintenance plan, approves vendors. Headquartered in Atlanta.")
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
        st.caption("ON-SITE")
        st.markdown("**LIFTBOT Deployed**")
        st.write("Material handling on scaffolding-heavy maintenance shutdowns")
        st.caption("Owner mandates create pull; contractor labor shortage creates push.")

st.caption(
    "**On channel tension:** Scaffold contractors bill by man-hour, so a labor-cutting "
    "robot can look like a margin threat. This resolves through two forces: (1) a "
    "structural labor shortage — they can't staff large shutdowns fully anyway — and (2) "
    "owner mandates, which reframe the contractor as a delivery channel, not a "
    "gatekeeper. BrandSafway's Alpharetta headquarters makes them the natural first "
    "partnership conversation in Georgia."
)
