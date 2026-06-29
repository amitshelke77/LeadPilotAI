import streamlit as st


def show_dashboard():
    # ----------------------------
    # Welcome Section
    # ----------------------------
    st.markdown("## 👋 Welcome back")
    st.write(
        "LeadPilot AI is ready. Select a module from the sidebar or launch one below."
    )

    st.divider()

    # ----------------------------
    # KPI Cards
    # ----------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📁 Projects",
            "0",
            help="Number of saved projects",
        )

    with col2:
        st.metric(
            "🏢 Leads Found",
            "0",
            help="Companies discovered",
        )

    with col3:
        st.metric(
            "⚙ Jobs Run",
            "0",
            help="Automation jobs executed",
        )

    with col4:
        st.metric(
            "📤 Exports",
            "0",
            help="Excel / CSV exports",
        )

    st.divider()

    # ----------------------------
    # Quick Modules
    # ----------------------------
    st.subheader("🚀 Launch Module")

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🏢 Company Finder",
            use_container_width=True,
        ):
            st.info("Coming in Sprint 3")

        if st.button(
            "🌐 Website Discovery",
            use_container_width=True,
        ):
            st.info("Coming Soon")

        if st.button(
            "📄 PDF Extractor",
            use_container_width=True,
        ):
            st.info("Coming Soon")

    with c2:
        if st.button(
            "📧 Email Finder",
            use_container_width=True,
        ):
            st.info("Coming Soon")

        if st.button(
            "🤖 AI Research",
            use_container_width=True,
        ):
            st.info("Coming Soon")

        if st.button(
            "📊 Export Center",
            use_container_width=True,
        ):
            st.info("Coming Soon")

    st.divider()

    # ----------------------------
    # Recent Jobs
    # ----------------------------
    st.subheader("📋 Recent Jobs")

    st.info(
        "No automation jobs have been executed yet."
    )

    st.divider()

    # ----------------------------
    # System Status
    # ----------------------------
    st.subheader("🟢 System Status")

    st.success("Application Loaded")

    st.success("Frontend Online")

    st.success("Ready for Automation")