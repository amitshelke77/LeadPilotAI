import streamlit as st

from frontend.dashboard import show_dashboard
from frontend.components.sidebar import show_sidebar
from frontend.components.header import show_header


st.set_page_config(
    page_title="LeadPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

page = show_sidebar()

show_header()

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "🏢 Company Search":
    st.title("🏢 Company Search")
    st.info("Coming in Sprint 2")

elif page == "🌐 Website Discovery":
    st.title("🌐 Website Discovery")
    st.info("Coming in Sprint 3")

elif page == "📧 Email Finder":
    st.title("📧 Email Finder")
    st.info("Coming in Sprint 4")

elif page == "📄 PDF Extractor":
    st.title("📄 PDF Extractor")
    st.info("Coming Soon")

elif page == "🤖 AI Research":
    st.title("🤖 AI Research")
    st.info("Coming Soon")

elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.info("Application settings will appear here.")

elif page == "ℹ️ About":
    st.title("About LeadPilot AI")

    st.write(
        """
LeadPilot AI is a modular business automation platform focused on:

- Lead Generation
- Company Research
- Website Scraping
- Email Extraction
- PDF Data Extraction
- AI Research
- Workflow Automation

Version: **0.1.0**
"""
    )