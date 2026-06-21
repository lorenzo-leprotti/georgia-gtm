import streamlit as st

st.set_page_config(
    page_title="KEWAZO | Georgia GTM",
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page("views/context_methodology.py", title="Context & Methodology", default=True),
    st.Page("views/strategy.py", title="GTM Strategy"),
    st.Page("views/map.py", title="Target Map"),
])
pg.run()
