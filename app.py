import streamlit as st
from pathlib import Path

from frontend.dashboard import show_dashboard
from frontend.company_finder import show_company_finder
from frontend.components.sidebar import show_sidebar
from frontend.components.header import show_header

st.set_page_config(
    page_title="LeadPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_css():
    css_file = Path("frontend/styles/main.css")
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

page = show_sidebar()
show_header()

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "🏢 Company Search":
    show_company_finder()

elif page == "🌐 Website Discovery":
    st.title("🌐 Website Discovery")
    st.info("Coming Soon")

elif page == "📧 Email Finder":
    st.title("📧 Email Finder")
    st.info("Coming Soon")

elif page == "📄 PDF Extractor":
    st.title("📄 PDF Extractor")
    st.info("Coming Soon")

elif page == "🤖 AI Research":
    st.title("🤖 AI Research")
    st.info("Coming Soon")

elif page == "⚙️ Settings":
    st.title("⚙️ Settings")

elif page == "ℹ️ About":
    st.title("About LeadPilot AI")
    st.write("LeadPilot AI v0.2.0")