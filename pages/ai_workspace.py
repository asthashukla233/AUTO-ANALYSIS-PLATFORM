import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from modules.analyst import analyze_data


def show_ai_workspace(df):

    # -----------------------------
    # SESSION STATE
    # -----------------------------

    if "working_df" not in st.session_state:

        st.session_state["working_df"] = (
            df.copy()
        )

    working_df = st.session_state[
        "working_df"
    ]

    # -----------------------------
    # OVERVIEW
    # -----------------------------

    st.subheader("🤖 AI Workspace")

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

    # -----------------------------
    # DATASET PREVIEW
    # -----------------------------

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        working_df.head(20),
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # DROPDOWNS
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        action = st.selectbox(
            "Action",
            [
                "None",
                "Drop Column",
                "Rename Column",
                "Convert To Sequential Numbers",
                "Multiply Column",
                "Divide Column",
                "Convert To Integer",
                "Convert To Float",
                "Convert To String",
                "Sort Ascending",
                "Sort Descending","Label Encoding"
                ,"One Hot Encoding"
            ]
        )

    with col2:

        selected_column = st.selectbox(
            "Column",
            working_df.columns.tolist()
        )

    with col3:

        ai_task = st.selectbox(
            "AI Analysis",
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

    # -----------------------------
    # EXTRA OPTIONS
    # -----------------------------

    new_name = ""
    numeric_value = 1.0

    if action == "Rename Column":

        new_name = st.text_input(
            "New Column Name"
        )

    elif action in [
        "Multiply Column",
        "Divide Column"
    ]:

        numeric_value = st.number_input(
            "Enter Value",
            value=1.0
        )

    st.divider()

    # -----------------------------
    # BUTTONS
    # -----------------------------

    b1, b2, b3 = st.columns(3)

    # -----------------------------
    # APPLY OPERATION
    # -----------------------------

    with b1:

        if st.button(
            "🛠 Apply Operation"
        ):

            try:

                if action == "Drop Column":

                    working_df.drop(
                        columns=[
                            selected_column
                        ],
                        inplace=True
                    )

                    st.success(
                        f"{selected_column} dropped."
                    )

                elif action == (
                    "Rename Column"
                ):

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
                        len(
                            working_df
                        ) + 1
                    )

                    st.success(
                        "Sequential numbers assigned."
                    )

                elif action == (
                    "Multiply Column"
                ):

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ]
                        * numeric_value
                    )

                    st.success(
                        "Column multiplied."
                    )

                elif action == (
                    "Divide Column"
                ):

                    working_df[
                        selected_column
                    ] = (
                        working_df[
                            selected_column
                        ]
                        / numeric_value
                    )

                    st.success(
                        "Column divided."
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
                        "Converted to Integer."
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
                        "Converted to Float."
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
                        "Converted to String."
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

                elif action == "Label Encoding":

                    le = LabelEncoder()

                    working_df[selected_column] = (
                        le.fit_transform(
                            working_df[selected_column]
                            .astype(str)
                        )
                    )

                    st.success(
                        "Label Encoding applied."
                    )

                elif action == "One-Hot Encoding":

                    encoded_df = pd.get_dummies(
                        working_df,
                        columns=[selected_column]
                    )

                    working_df = encoded_df

                    st.success(
                        "One-Hot Encoding applied."
                    )    
                st.session_state[
                    "working_df"
                ] = working_df

            except Exception as e:

                st.error(
                    str(e)
                )

    # -----------------------------
    # AI ANALYSIS
    # -----------------------------

    with b2:

        if st.button(
            "🤖 Run AI Analysis"
        ):

            if ai_task != "None":

                with st.spinner(
                    "Analyzing..."
                ):

                    result = analyze_data(
                        working_df,
                        ai_task
                    )

                st.subheader(
                    "AI Result"
                )

                st.write(
                    result
                )

    # -----------------------------
    # RESET
    # -----------------------------

    with b3:

        if st.button(
            "🔄 Reset Dataset"
        ):

            st.session_state[
                "working_df"
            ] = df.copy()

            st.rerun()

    st.divider()

    # -----------------------------
    # UPDATED DATASET
    # -----------------------------

    st.subheader(
        "📄 Updated Dataset"
    )

    st.dataframe(
        st.session_state[
            "working_df"
        ].head(20),
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # DOWNLOAD
    # -----------------------------

    csv = (
        st.session_state[
            "working_df"
        ]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        "⬇ Download Dataset",
        csv,
        "updated_dataset.csv",
        "text/csv"
    )