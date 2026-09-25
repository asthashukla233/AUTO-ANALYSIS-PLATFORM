import streamlit as st
import pandas as pd

from modules.loader import load_file
from modules.analyst import analyze_data

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Data Workspace",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("📊 AI Data Workspace")

st.write(
    "Upload a dataset, perform data operations, and get AI-powered insights."
)

# ----------------------------------
# FILE UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# ----------------------------------
# MAIN APP
# ----------------------------------

if uploaded_file:

    df = load_file(uploaded_file)

    # Session State

    if "working_df" not in st.session_state:

        st.session_state["working_df"] = (
            df.copy()
        )

    working_df = st.session_state[
        "working_df"
    ]

    # ----------------------------------
    # DATASET OVERVIEW
    # ----------------------------------

    st.subheader("📊 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        working_df.shape[0]
    )

    c2.metric(
        "Columns",
        working_df.shape[1]
    )

    c3.metric(
        "Missing Values",
        working_df.isnull().sum().sum()
    )

    c4.metric(
        "Duplicates",
        working_df.duplicated().sum()
    )

    st.divider()

    # ----------------------------------
    # DATASET PREVIEW
    # ----------------------------------

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        working_df.head(20),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------
    # DATA OPERATIONS
    # ----------------------------------

    st.subheader("🛠 Data Operations")

    col1, col2, col3 = st.columns(3)

    with col1:

        action = st.selectbox(
            "Select Action",
            [
                "None",
                "Drop Column",
                "Rename Column",
                "Convert To Sequential Numbers",
                "Multiply Column",
                "Divide Column",
                "Remove Duplicates",
                "Fill Missing Values",
                "Convert To Integer",
                "Convert To Float",
                "Convert To String",
                "Sort Ascending",
                "Sort Descending"
            ]
        )

    with col2:

        selected_column = st.selectbox(
            "Select Column",
            working_df.columns.tolist()
        )

    with col3:

        ai_task = st.selectbox(
            "AI Assistant",
            [
                "None",
                "Dataset Summary",
                "Business Insights",
                "Trend Analysis",
                "Customer Insights",
                "Anomaly Detection",
                "Data Quality Report",
                "Correlation Analysis",
                "Visualization Suggestions",
                "Executive Report"
            ]
        )

    # ----------------------------------
    # DYNAMIC OPTIONS
    # ----------------------------------

    st.subheader("⚙ Additional Options")

    new_name = ""
    numeric_value = 1.0
    fill_method = "Mean"

    if action == "Rename Column":

        new_name = st.text_input(
            "Enter New Column Name"
        )

    elif action in [
        "Multiply Column",
        "Divide Column"
    ]:

        numeric_value = st.number_input(
            "Enter Value",
            value=1.0
        )

    elif action == "Fill Missing Values":

        fill_method = st.selectbox(
            "Fill Method",
            [
                "Mean",
                "Median",
                "Mode"
            ]
        )

    st.divider()

    # ----------------------------------
    # BUTTONS
    # ----------------------------------

    b1, b2, b3 = st.columns(3)

    # ----------------------------------
    # APPLY OPERATION
    # ----------------------------------

    with b1:

        if st.button("🛠 Apply Operation"):

            try:

                if action == "Drop Column":

                    working_df.drop(
                        columns=[selected_column],
                        inplace=True
                    )

                    st.success(
                        f"{selected_column} dropped."
                    )

                elif action == "Rename Column":

                    working_df.rename(
                        columns={
                            selected_column:
                            new_name
                        },
                        inplace=True
                    )

                    st.success(
                        "Column renamed."
                    )

                elif action == (
                    "Convert To Sequential Numbers"
                ):

                    working_df[
                        selected_column
                    ] = range(
                        1,
                        len(working_df)+1
                    )

                    st.success(
                        "Sequential numbers assigned."
                    )

                elif action == "Multiply Column":

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ] * numeric_value
                    )

                    st.success(
                        "Column multiplied."
                    )

                elif action == "Divide Column":

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ] / numeric_value
                    )

                    st.success(
                        "Column divided."
                    )

                elif action == (
                    "Remove Duplicates"
                ):

                    working_df = (
                        working_df
                        .drop_duplicates()
                    )

                    st.success(
                        "Duplicates removed."
                    )

                elif action == (
                    "Fill Missing Values"
                ):

                    if fill_method == "Mean":

                        working_df[
                            selected_column
                        ] = (
                            working_df[
                                selected_column
                            ]
                            .fillna(
                                working_df[
                                    selected_column
                                ]
                                .mean()
                            )
                        )

                    elif fill_method == (
                        "Median"
                    ):

                        working_df[
                            selected_column
                        ] = (
                            working_df[
                                selected_column
                            ]
                            .fillna(
                                working_df[
                                    selected_column
                                ]
                                .median()
                            )
                        )

                    elif fill_method == (
                        "Mode"
                    ):

                        working_df[
                            selected_column
                        ] = (
                            working_df[
                                selected_column
                            ]
                            .fillna(
                                working_df[
                                    selected_column
                                ]
                                .mode()[0]
                            )
                        )

                    st.success(
                        "Missing values filled."
                    )

                elif action == (
                    "Convert To Integer"
                ):

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ]
                        .astype(int)
                    )

                    st.success(
                        "Converted to integer."
                    )

                elif action == (
                    "Convert To Float"
                ):

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ]
                        .astype(float)
                    )

                    st.success(
                        "Converted to float."
                    )

                elif action == (
                    "Convert To String"
                ):

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ]
                        .astype(str)
                    )

                    st.success(
                        "Converted to string."
                    )

                elif action == (
                    "Sort Ascending"
                ):

                    working_df = (
                        working_df
                        .sort_values(
                            selected_column
                        )
                    )

                    st.success(
                        "Sorted ascending."
                    )

                elif action == (
                    "Sort Descending"
                ):

                    working_df = (
                        working_df
                        .sort_values(
                            selected_column,
                            ascending=False
                        )
                    )

                    st.success(
                        "Sorted descending."
                    )

                st.session_state[
                    "working_df"
                ] = working_df

            except Exception as e:

                st.error(str(e))

    # ----------------------------------
    # RUN AI
    # ----------------------------------

    with b2:

        if st.button("🤖 Run AI Analysis"):

            if ai_task != "None":

                with st.spinner(
                    "Analyzing dataset..."
                ):

                    result = analyze_data(
                        working_df,
                        ai_task
                    )

                st.subheader(
                    "🤖 AI Analysis"
                )

                st.write(result)

    # ----------------------------------
    # RESET
    # ----------------------------------

    with b3:

        if st.button(
            "🔄 Reset Dataset"
        ):

            st.session_state[
                "working_df"
            ] = df.copy()

            st.rerun()

    st.divider()

    # ----------------------------------
    # UPDATED DATASET
    # ----------------------------------

    st.subheader(
        "📋 Updated Dataset"
    )

    st.dataframe(
        st.session_state[
            "working_df"
        ].head(20),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------
    # DOWNLOAD
    # ----------------------------------

    csv = (
        st.session_state[
            "working_df"
        ]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="⬇ Download Updated Dataset",
        data=csv,
        file_name="updated_dataset.csv",
        mime="text/csv"
    )

else:

    st.info(
        "📂 Upload a CSV or Excel file to begin."
    )
