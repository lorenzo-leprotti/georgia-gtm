import streamlit as st

st.header("How This Was Built")

st.markdown(
    "A short account of the method. The point is not the conclusion alone, "
    "but that it was reached in a structured, verifiable way."
)

method_items = [
    ("The question", "Could Georgia be KEWAZO's next US industrial market, and which sites would you target first? Scope deliberately bounded: scaffolding-intensive maintenance turnarounds in process industries as the beachhead, construction boom as the timing wedge."),
    ("Spec before build", "Started with a PRD, not code. Defined purpose, audience, scope, and explicit out-of-scope before anything was built. Strategy drives the artifact, not the other way around."),
    ("Verification", "Every factual claim verified with source + date. Rules: no source → no row. Closed mills removed. Rounded coordinates corrected against authoritative sources (Global Energy Monitor, Wikipedia infobox, official addresses). Confidence flagged per row. Weak citations upgraded (GP Brunswick moved from county Facebook post to Pulp and Paper Chronicle trade press)."),
    ("The buyer model", "Held as an explicit assumption, then tested. Research confirmed: dual buyer (owner specs-in, contractor deploys), two contracting structures (direct and through turnaround management contractor), with BrandSafway as the dominant Georgia-market channel. Value quantified: 15–25% of TAR labor is scaffolding; LIFTBOT's ~70% material-handling reduction → 10–17% total TAR labor cost reduction."),
    ("Tools", "Reasoning and PRD: Claude. Fact verification: Perplexity (deep research). Data: portable CSV, one row per site, decoupled from code. Delivery: Streamlit + pydeck."),
    ("Honest boundaries", "The buyer model is research-confirmed for the sector, not validated inside KEWAZO. GP Rincon TAR cadence has no confirmed public schedule (confidence: medium). Tier 3 sites are completeness, not live targets. These are flagged rather than hidden."),
]

for label, body in method_items:
    with st.expander(label.upper()):
        st.write(body)

st.divider()
st.caption("Lorenzo Leprotti · June 2026 · All data sourced and verified · Built with Streamlit + pydeck")
