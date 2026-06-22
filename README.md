# KEWAZO Georgia GTM Strategy

An interactive Streamlit app arguing that Georgia is KEWAZO's next US industrial expansion
market. Built as a research artifact for the KEWAZO interview process: a structured,
sourced go-to-market thesis that works as a live screen-share or as a sent link.

**Live app:** https://georgia-gtm-uuapqbzsh7cx2nwqpo9yjn.streamlit.app/

## What it is

Three pages, one argument:

1. **Context & Methodology** : the thesis, how the analysis was built, and the dual buyer
   model.
2. **GTM Strategy** : the problem, Georgia's industrial maintenance market (with bottom-up
   sizing), why Georgia, the first move, and the buyer model end to end.
3. **Target Map** : 19 Georgia targets plotted and color-coded by tier.

The core argument: recurring process-industry maintenance shutdowns (pulp and paper, power)
are the entry point, the construction boom is the timing wedge, and the buyer chain (asset
owner approves, scaffold-access contractor deploys) sits almost entirely in metro Atlanta.

## Data

All site data is verified with a source URL and date per row before it enters
`data/sites.csv`: 19 sites across 3 tiers (8 Tier 1, 6 Tier 2, 5 Tier 3). The methodology,
buyer model, market sizing math, and the reference check that corrected several early
figures are written up in [`RESEARCH_NOTES.md`](RESEARCH_NOTES.md).

## Repo structure

```
KEWAZO_GTM_Georgia/
|- app.py                          # entry point: page config + navigation
|- views/
|  |- context_methodology.py       # page 1
|  |- strategy.py                  # page 2
|  |- map.py                       # page 3
|- data/
|  |- sites.csv                    # verified target list, one sourced row per site
|- RESEARCH_NOTES.md               # methodology, buyer model, sizing, reference check
|- requirements.txt
|- pyproject.toml
|- uv.lock
|- .streamlit/config.toml
```

## Run locally

With [uv](https://docs.astral.sh/uv/):

```
uv sync
uv run streamlit run app.py
```

Or with pip:

```
pip install -r requirements.txt
streamlit run app.py
```

Stack: Streamlit (multi-page via `st.navigation`), pydeck for the map (CARTO basemap, no API
token needed), pandas.

---

A targeted market entry analysis. Lorenzo Leprotti, June 2026.
