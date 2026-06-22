import streamlit as st

from modules.visualizer import (
    create_histogram,
    create_boxplot,
    create_bar_chart,
    create_line_chart,
    create_scatter_plot,
    create_pie_chart,
    create_heatmap
)


def show_visualization(df):

    st.subheader(
        "📊 Data Visualization"
    )

    chart_type = st.selectbox(
        "Select Chart Type",
        [
            "Histogram",
            "Box Plot",
            "Bar Chart",
            "Line Chart",
            "Scatter Plot",
            "Pie Chart",
            "Correlation Heatmap"
        ]
    )

    all_columns = df.columns.tolist()

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    # -------------------------
    # Histogram
    # -------------------------

    if chart_type == "Histogram":

        if len(numeric_cols) == 0:

            st.warning(
                "No numeric columns found."
            )

            return

        column = st.selectbox(
            "Select Column",
            numeric_cols
        )

        fig = create_histogram(
            df,
            column
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Box Plot
    # -------------------------

    elif chart_type == "Box Plot":

        if len(numeric_cols) == 0:

            st.warning(
                "No numeric columns found."
            )

            return

        column = st.selectbox(
            "Select Column",
            numeric_cols
        )

        fig = create_boxplot(
            df,
            column
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Pie Chart
    # -------------------------

    elif chart_type == "Pie Chart":

        categorical_cols = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        if len(categorical_cols) == 0:

            st.warning(
                "No categorical columns found."
            )

            return

        column = st.selectbox(
            "Select Column",
            categorical_cols
        )

        fig = create_pie_chart(
            df,
            column
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Bar Chart
    # -------------------------

    elif chart_type == "Bar Chart":

        col1, col2 = st.columns(2)

        with col1:

            x_col = st.selectbox(
                "X Axis",
                all_columns
            )

        with col2:

            y_col = st.selectbox(
                "Y Axis",
                numeric_cols
            )

        grouped = (
            df.groupby(x_col)[y_col]
            .mean()
            .reset_index()
        )

        fig = create_bar_chart(
            grouped,
            x_col,
            y_col
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Line Chart
    # -------------------------

    elif chart_type == "Line Chart":

        col1, col2 = st.columns(2)

        with col1:

            x_col = st.selectbox(
                "X Axis",
                all_columns
            )

        with col2:

            y_col = st.selectbox(
                "Y Axis",
                numeric_cols
            )

        fig = create_line_chart(
            df,
            x_col,
            y_col
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Scatter Plot
    # -------------------------

    elif chart_type == "Scatter Plot":

        col1, col2 = st.columns(2)

        with col1:

            x_col = st.selectbox(
                "X Axis",
                numeric_cols
            )

        with col2:

            y_col = st.selectbox(
                "Y Axis",
                numeric_cols
            )

        fig = create_scatter_plot(
            df,
            x_col,
            y_col
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # Heatmap
    # -------------------------

    elif chart_type == "Correlation Heatmap":

        fig = create_heatmap(df)

        st.plotly_chart(
            fig,
            use_container_width=True
        )