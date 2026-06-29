import streamlit as st


def show_dashboard():
    st.title("🚀 LeadPilot AI")

    st.caption("AI Powered Business Automation Platform")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Projects",
            value="0"
        )

    with col2:
        st.metric(
            label="Jobs Completed",
            value="0"
        )

    with col3:
        st.metric(
            label="Exports",
            value="0"
        )

    st.divider()

    st.subheader("📋 Recent Activity")

    st.info("No jobs have been executed yet.")

    st.divider()

    st.subheader("⚡ Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "➕ New Job",
            use_container_width=True
        )

    with c2:
        st.button(
            "📄 Documentation",
            use_container_width=True
        )

    with c3:
        st.button(
            "📜 View Logs",
            use_container_width=True
        )