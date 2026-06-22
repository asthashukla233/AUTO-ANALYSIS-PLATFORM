import streamlit as st

from modules.loader import load_file

from pages.overview import show_overview
from pages.cleaning import show_cleaning
from pages.visualization import show_visualization
from pages.ai_workspace import show_ai_workspace

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Personal Data Analyzer",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("📊 Personal Data Analyzer")

st.write(
    """
    Upload a CSV or Excel file and explore,
    clean, visualize, edit and analyze your data.
    """
)

# ----------------------------------
# FILE UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

# ----------------------------------
# MAIN APP
# ----------------------------------

if uploaded_file:

    df = load_file(uploaded_file)

    st.success(
        "✅ File Uploaded Successfully!"
    )

    # ----------------------------------
    # TABS
    # ----------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Overview",
            "🧹 Cleaning",
            "📈 Visualizations",
            "🤖 AI Workspace"
        ]
    )

    # ----------------------------------
    # OVERVIEW
    # ----------------------------------

    with tab1:

        show_overview(df)

    # ----------------------------------
    # CLEANING
    # ----------------------------------

    with tab2:

        show_cleaning(df)

    # ----------------------------------
    # VISUALIZATION
    # ----------------------------------

    with tab3:

        show_visualization(df)

    # ----------------------------------
    # AI WORKSPACE
    # ----------------------------------

    with tab4:

        show_ai_workspace(df)

# ----------------------------------
# NO FILE
# ----------------------------------

else:

    st.info(
        "📂 Upload a CSV or Excel file to begin."
    )