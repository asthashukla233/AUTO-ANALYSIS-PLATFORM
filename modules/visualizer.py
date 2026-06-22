import plotly.express as px
import plotly.graph_objects as go


def create_histogram(df, column):

    return px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )


def create_boxplot(df, column):

    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )


def create_bar_chart(df, x_col, y_col):

    return px.bar(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} by {x_col}"
    )


def create_line_chart(df, x_col, y_col):

    return px.line(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} over {x_col}"
    )


def create_scatter_plot(df, x_col, y_col):

    return px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )


def create_pie_chart(df, column):

    counts = df[column].value_counts()

    return px.pie(
        values=counts.values,
        names=counts.index,
        title=f"Distribution of {column}"
    )


def create_heatmap(df):

    corr = df.select_dtypes(
        include="number"
    ).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig