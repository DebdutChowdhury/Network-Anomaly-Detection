import streamlit as st

def home_page():
    st.image("bkg.png", use_container_width=True)
    st.title("Home")
    st.write('Welcome to the Network Anomaly Detection App!')

    st.markdown("""
    <div style="position: relative; padding-bottom: 56.22254758418741%; height: 0;">
                <iframe src="https://www.loom.com/embed/9a92381c60ef4ccd8e809a21baebb112?sid=5978733f-b424-46c6-a616-0591ec02a269" 
                    frameborder="0" 
                    webkitallowfullscreen 
                    mozallowfullscreen 
                    allowfullscreen 
                    style="position: absolute; 
                    top: 0; left: 0; width: 100%; height: 100%;">
                    </iframe>
    </div>
    """, unsafe_allow_html=True)