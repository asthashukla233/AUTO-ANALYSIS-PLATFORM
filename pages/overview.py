import streamlit as st
import pandas as pd

from modules.profiler import get_profile


def show_overview(df):

    profile = get_profile(df)

    # ----------------------------------
    # DATASET SUMMARY
    # ----------------------------------

    st.subheader("📈 Dataset Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", profile["Rows"])
    col2.metric("Columns", profile["Columns"])
    col3.metric("Missing Values", profile["Missing Values"])
    col4.metric("Duplicates", profile["Duplicate Rows"])
    col5.metric(
        "Memory (MB)",
        profile["Memory Usage (MB)"]
    )

    st.divider()

    # ----------------------------------
    # DATA PREVIEW
    # ----------------------------------

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------
    # COLUMN INFORMATION
    # ----------------------------------

    st.subheader("🧾 Column Information")

    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(
        column_info,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------
    # MISSING VALUES
    # ----------------------------------

    st.subheader("⚠ Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum().values
    })

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.write(
        f"**Total Missing Values:** {df.isnull().sum().sum()}"
    )