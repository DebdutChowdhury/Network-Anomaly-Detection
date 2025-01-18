import streamlit as st

def home_page():
    st.image("bkg.png", use_container_width=True)
    st.title("Home")
    st.write('Welcome to the Network Anomaly Detection App!')

    st.markdown("""
    <div style="position: relative; padding-bottom: 64.98194945848375%; height: 0;">
        loom video
    </div>
    """, unsafe_allow_html=True)