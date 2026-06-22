import streamlit as st

from modules.cleaner import clean_data
from modules.profiler import get_profile


def show_cleaning(df):

    st.subheader("🧹 Data Cleaning")

    st.write(
        "Clean missing values and remove duplicate records."
    )

    if st.button("Clean My Data"):

        missing_before = df.isnull().sum().sum()

        duplicates_before = df.duplicated().sum()

        cleaned_df = clean_data(df)

        missing_after = cleaned_df.isnull().sum().sum()

        duplicates_after = cleaned_df.duplicated().sum()

        st.success(
            "✅ Dataset Cleaned Successfully!"
        )

        # ------------------------------
        # Cleaning Report
        # ------------------------------

        st.subheader("📄 Cleaning Report")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Missing Before",
                int(missing_before)
            )

            st.metric(
                "Duplicates Before",
                int(duplicates_before)
            )

        with col2:
            st.metric(
                "Missing After",
                int(missing_after)
            )

            st.metric(
                "Duplicates After",
                int(duplicates_after)
            )

        st.divider()

        # ------------------------------
        # Cleaned Preview
        # ------------------------------

        st.subheader(
            "🧼 Cleaned Dataset Preview"
        )

        st.dataframe(
            cleaned_df.head(),
            use_container_width=True
        )

        st.divider()

        # ------------------------------
        # Cleaned Summary
        # ------------------------------

        cleaned_profile = get_profile(
            cleaned_df
        )

        st.subheader(
            "📊 Cleaned Dataset Summary"
        )

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric(
            "Rows",
            cleaned_profile["Rows"]
        )

        c2.metric(
            "Columns",
            cleaned_profile["Columns"]
        )

        c3.metric(
            "Missing Values",
            cleaned_profile["Missing Values"]
        )

        c4.metric(
            "Duplicates",
            cleaned_profile["Duplicate Rows"]
        )

        c5.metric(
            "Memory (MB)",
            cleaned_profile["Memory Usage (MB)"]
        )

        st.divider()

        # ------------------------------
        # Download Cleaned Dataset
        # ------------------------------

        csv = cleaned_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )