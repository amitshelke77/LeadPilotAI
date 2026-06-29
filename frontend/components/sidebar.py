import streamlit as st


def show_sidebar():
    with st.sidebar:
        st.title("🚀 LeadPilot AI")
        st.caption("Business Automation Platform")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "🏢 Company Search",
                "🌐 Website Discovery",
                "📧 Email Finder",
                "📄 PDF Extractor",
                "🤖 AI Research",
                "⚙️ Settings",
                "ℹ️ About",
            ],
        )

        st.divider()

        st.success("System Status: Online")

        return page