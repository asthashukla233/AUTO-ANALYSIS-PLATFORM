from langchain_ollama import ChatOllama

# Faster model for dashboard analysis
llm = ChatOllama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434",
    temperature=0
)


def analyze_data(df, task):

    context = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.astype(str).to_dict()}
"""

    # ----------------------------------
    # DATASET SUMMARY
    # ----------------------------------

    if task == "Dataset Summary":

        prompt = f"""
You are a Senior Data Analyst.

Dataset Metadata:

{context}

Provide:

1. Dataset overview
2. Important columns
3. Potential use cases

Keep answer concise.
"""

    # ----------------------------------
    # BUSINESS INSIGHTS
    # ----------------------------------

    elif task == "Business Insights":

        prompt = f"""
You are a Senior Business Analyst.

Dataset Metadata:

{context}

Provide:

1. Business opportunities
2. Important KPIs
3. Risks
4. Recommendations

Keep answer under 250 words.
"""

    # ----------------------------------
    # TREND ANALYSIS
    # ----------------------------------

    elif task == "Trend Analysis":

        prompt = f"""
You are a Senior Data Analyst.

Dataset Metadata:

{context}

Identify:

1. Possible trends
2. Interesting patterns
3. What should be investigated further

Keep answer concise.
"""

    # ----------------------------------
    # CUSTOMER INSIGHTS
    # ----------------------------------

    elif task == "Customer Insights":

        prompt = f"""
You are a Customer Analytics Expert.

Dataset Metadata:

{context}

Provide:

1. Customer-related observations
2. Segmentation ideas
3. Retention opportunities

Keep answer concise.
"""

    # ----------------------------------
    # ANOMALIES
    # ----------------------------------

    elif task == "Anomaly Detection":

        prompt = f"""
You are a Data Quality Expert.

Dataset Metadata:

{context}

Suggest:

1. Possible anomalies
2. Suspicious columns
3. Data validation checks

Keep answer concise.
"""

    # ----------------------------------
    # DATA QUALITY
    # ----------------------------------

    elif task == "Data Quality Report":

        prompt = f"""
You are a Data Quality Expert.

Dataset Metadata:

{context}

Evaluate:

1. Missing values risk
2. Duplicate risks
3. Data type issues
4. Cleaning recommendations

Keep answer concise.
"""

    # ----------------------------------
    # CORRELATION
    # ----------------------------------

    elif task == "Correlation Analysis":

        prompt = f"""
You are a Data Scientist.

Dataset Metadata:

{context}

Suggest:

1. Which columns may correlate
2. Useful relationships to investigate
3. Recommended analyses

Keep answer concise.
"""

    # ----------------------------------
    # VISUALIZATION
    # ----------------------------------

    elif task == "Visualization Suggestions":

        prompt = f"""
You are a BI Expert.

Dataset Metadata:

{context}

Recommend:

1. Best charts
2. Why they are useful
3. Which columns should be used

Keep answer concise.
"""

    # ----------------------------------
    # EXECUTIVE REPORT
    # ----------------------------------

    elif task == "Executive Report":

        prompt = f"""
You are a Senior Data Consultant.

Dataset Metadata:

{context}

Generate an executive summary.

Include:

1. Overview
2. Key findings
3. Recommendations

Keep under 400 words.
"""

    else:

        prompt = f"""
Dataset:

{context}

Task:

{task}
"""

    response = llm.invoke(prompt)

    return response.content