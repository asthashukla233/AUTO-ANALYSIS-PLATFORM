# 📊 Personal Data Analyzer

An AI-powered data analytics platform built with **Streamlit, Pandas, Plotly, Scikit-Learn, and Ollama (Llama 3.2)** that enables users to upload datasets, clean data, generate visualizations, perform preprocessing operations, and obtain AI-driven analytical insights through a user-friendly interface.

---

## 🚀 Features

### 📊 Dataset Overview

* View dataset dimensions
* Missing value statistics
* Duplicate row detection
* Dataset preview
* Column information

### 🧹 Data Cleaning

* Missing value analysis
* Duplicate detection
* Automated cleaning workflow
* Download cleaned dataset

### 📈 Interactive Visualizations

* Histogram
* Box Plot
* Bar Chart
* Line Chart
* Scatter Plot
* Pie Chart
* Correlation Heatmap

### 🤖 AI Workspace

Perform data transformation and analysis without writing code.

#### Data Operations

* Drop Column
* Rename Column
* Convert to Sequential Numbers
* Multiply Column
* Divide Column
* Convert to Integer
* Convert to Float
* Convert to String
* Sort Ascending
* Sort Descending
* Label Encoding
* One-Hot Encoding

#### AI Analysis (Llama 3.2 + Ollama)

* Dataset Summary
* Business Insights
* Trend Analysis
* Customer Insights
* Anomaly Detection
* Data Quality Report
* Correlation Analysis
* Visualization Suggestions
* Executive Report

### 📥 Export Features

* Download transformed dataset
* Save processed data for further analysis

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Machine Learning

* Scikit-Learn

### AI Integration

* Ollama
* Llama 3.2

---

## 📂 Project Structure

```bash
personal-data-analyzer/
│
├── app.py
│
├── modules/
│   ├── loader.py
│   ├── cleaner.py
│   ├── profiler.py
│   ├── visualizer.py
│   └── analyst.py
│
├── pages/
│   ├── overview.py
│   ├── cleaning.py
│   ├── visualization.py
│   └── ai_workspace.py
│
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/personal-data-analyzer.git
cd personal-data-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama

Install Ollama:

https://ollama.com

Pull Llama 3.2:

```bash
ollama pull llama3.2
```

Start Ollama:

```bash
ollama serve
```

Verify Installation:

```bash
ollama list
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## 📸 Screenshots

### Dataset Overview

<img width="1752" height="866" alt="image" src="https://github.com/user-attachments/assets/1d5fc359-c821-4dd3-9420-e01b2d961bf9" />


### Data Cleaning

<img width="1753" height="840" alt="image" src="https://github.com/user-attachments/assets/65da7d35-d972-417c-a1ad-f9e1cadea559" />


### Visualizations

<img width="1821" height="901" alt="image" src="https://github.com/user-attachments/assets/dd4e0192-a0c8-4612-9cd2-5182907c4a6d" />


### AI Workspace

<img width="1820" height="713" alt="image" src="https://github.com/user-attachments/assets/26829522-b168-4fca-9052-713ffe77591b" />
<img width="1817" height="725" alt="image" src="https://github.com/user-attachments/assets/a6b08d5c-79a6-4b54-ac53-3d76fd2600b5" />


---

## 🎯 Use Cases

* Exploratory Data Analysis (EDA)
* Business Intelligence
* Data Cleaning & Preprocessing
* Feature Engineering
* Dataset Transformation
* AI-Assisted Analytics
* Educational Data Science Projects

---

## 🔮 Future Enhancements

* PDF Report Generation
* AI-Powered Cleaning Recommendations
* Automated Dashboard Generation
* Advanced Statistical Analysis
* Multi-File Analysis
* RAG-Based Dataset Question Answering
* Cloud Deployment Support
* Natural Language Data Editing

---

## 💡 Key Highlights

* No coding required for common data operations
* Interactive visual analytics
* Local AI-powered analysis using Ollama
* End-to-end data preprocessing workflow
* Beginner-friendly user interface
* Modular and scalable architecture

---

## 👩‍💻 Author

**Astha Shukla**

Computer Science Engineer | Data Science & AI Enthusiast

Focused on Machine Learning, Data Analytics, Computer Vision, and AI-powered Applications.

---

## ⭐ If you found this project useful, consider giving it a star!
