# KEWAZO Georgia GTM Strategy

Interactive Streamlit app arguing Georgia as KEWAZO's next US industrial expansion market. Built as a proactive differentiator for the KEWAZO interview process. Deploys to Streamlit Cloud; usable as a live screen-share or a sent link.

## What it is
- **Methodology + strategy (text):** thesis, dual buyer model, ICP scoring rubric, entry sequence.
- **Map (visual hero):** Georgia targets plotted, color-coded by tier.
- Full spec: see [`PRD.md`](PRD.md).

## Repo structure
```
KEWAZO_GTM_Georgia/
├── PRD.md                   # product requirements / spec (source of truth)
├── DATA_RESEARCH_PROMPT.md  # Perplexity prompt + CSV schema for the data layer
├── buyer_chain_notes.md     # verified buyer-chain + turnaround research, with sources
├── requirements.txt
├── .gitignore
└── data/
    └── sites.csv            # verified target list (one row per site, sourced)
```
(`app.py` to be created in Claude Code per PRD milestones.)

## Data
All site data is verified in Perplexity (source + date per row) before entering `data/sites.csv`. 19 sites across 3 tiers. Buyer-chain and turnaround research with full sourcing lives in `buyer_chain_notes.md`.

## Status
Pre-build, data layer complete. Next: build the app in Claude Code (plan mode) from `PRD.md`, reading `data/sites.csv`.

## Run locally (once app.py exists)
```
pip install -r requirements.txt
streamlit run app.py
```
