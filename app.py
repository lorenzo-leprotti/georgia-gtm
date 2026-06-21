import streamlit as st

st.set_page_config(
    page_title="KEWAZO | Georgia GTM",
    page_icon="🏗",
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page("views/strategy.py", title="Strategy & Map", icon="🗺️", default=True),
    st.Page("views/methodology.py", title="Methodology", icon="🧭"),
])
pg.run()
