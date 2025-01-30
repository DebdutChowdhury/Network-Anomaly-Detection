import streamlit as st
import importlib.util

# Dummy user credentials
USERNAME = "admin"
PASSWORD = "admin"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'dummy' not in st.session_state:
    st.session_state.dummy = 0

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        st.session_state.logged_in = True
        st.session_state.dummy += 1
    else:
        st.error("Invalid username or password")

def logout():
    st.session_state.logged_in = False
    st.session_state.dummy += 1



def login_page():
    st.image("bkg.png", use_container_width=True)
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)

def main():
    # login page and home page
    if st.session_state.logged_in:
        page = st.sidebar.selectbox("Select a page", ["Home", "Security Scan", "Reports"])
        st.write(page)
        if page == "Home":
            spec = importlib.util.spec_from_file_location("home.py", "home.py")
            home_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(home_module)
            home_module.home_page()
            if st.sidebar.button("Logout"):
                logout()

        # Security scan page or model implementation page
        elif page == "Security Scan":
            spec = importlib.util.spec_from_file_location("model.py", "model.py")
            ml_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(ml_module)
            ml_module.detection_page()
            if st.sidebar.button("Logout"):
                logout()

        # Reports page
        elif page == "Reports":
            spec = importlib.util.spec_from_file_location("report.py", "report.py")
            reports_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(reports_module)
            reports_module.reports_page()
            if st.sidebar.button("Logout"):
                logout()
    else:
        login_page()

    footer_html = """<div style='text-align: center;'>
    <p>Developed by ❤️ Debdut Chowdhury</p>
    </div>"""
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()