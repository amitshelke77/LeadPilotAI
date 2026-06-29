import streamlit as st

from backend.services.company_search import search_companies
from backend.services.exporter import export_to_excel


def show_company_finder():
    st.title("🏢 Company Finder")

    if "companies_df" not in st.session_state:
        st.session_state.companies_df = None

    col1, col2 = st.columns(2)

    with col1:
        industry = st.text_input(
            "Industry",
            placeholder="Plastic Manufacturers",
        )

    with col2:
        location = st.text_input(
            "Location",
            placeholder="Pune",
        )

    max_results = st.slider(
        "Maximum Results",
        10,
        500,
        100,
        step=10,
    )

    if st.button("🚀 Start Search", use_container_width=True):

        if not industry or not location:
            st.warning("Please enter both Industry and Location.")
            return

        with st.spinner("Searching..."):
            df = search_companies(
                industry,
                location,
                max_results,
            )

        st.session_state.companies_df = df

    if st.session_state.companies_df is not None:

        df = st.session_state.companies_df

        st.success(f"Found {len(df)} companies")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        filepath = export_to_excel(df)

        with open(filepath, "rb") as file:
            st.download_button(
                "📥 Download Excel",
                data=file,
                file_name=filepath.name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
            )