import streamlit as st

# ── METHODOLOGY ─────────────────────────────────────────────────────────────
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

# ── AUTOMATION SUBSECTION ───────────────────────────────────────────────────
st.header("Hypothetical Execution Flow")

st.markdown(
    "The GTM motion is sequenced, not automated — but the execution layer is "
    "tool-agnostic. Below is a hypothetical workflow showing how Lorenzo would "
    "instrument the outreach and follow-up cycle. **This is a delivery "
    "assumption, not a KEWAZO system.** Swapping Make for n8n (or the reverse) "
    "is a configuration change, not a strategy change."
)

flow_steps = [
    ("Trigger", "TAR schedule alert", "Monitor trade press (Pulp & Paper Chronicle, Fastmarkets, Global Energy Monitor) for announced outage windows. Trigger: new TAR date confirmed at a Tier 1 site."),
    ("Enrich", "Site + owner lookup", "Pull owner contact, recent TAR history, and BrandSafway contract status from internal CRM. Flag if BrandSafway is the incumbent contractor."),
    ("Route", "Dual-track outreach", "Route to (A) owner-level KEWAZO account team for spec-in conversation and (B) BrandSafway regional manager for deployment coordination."),
    ("Track", "Pipeline entry + follow-up", "Log TAR date, site, and outreach status. Auto-reminder 90 days before outage window for pre-mobilization check-in."),
    ("Capture", "Post-deployment data", "After deployment: log LIFTBOT hours, scaffold-hours avoided, crew headcount. Feed back to KEWAZO's ROI documentation."),
]

for trigger, label, desc in flow_steps:
    with st.container(border=True):
        st.caption(trigger)
        st.markdown(f"**{label}**")
        st.write(desc)

st.caption(
    "Tool stack assumption: Make (or n8n) for orchestration · HubSpot / "
    "Pipedrive for CRM · Notion for TAR calendar tracking. None of this "
    "requires custom software — it's a configured workflow, deployable in a week."
)

st.divider()
st.caption(
    "Lorenzo Leprotti · June 2026 · All data sourced and verified · "
    "Built with Streamlit + pydeck"
)
