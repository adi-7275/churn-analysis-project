# 📊 Customer Churn Analysis and Customer Intelligence

## 📌 Project Overview

Customer Churn Analysis is a data analytics project that analyzes customer behavior, identifies churn patterns, and generates business insights to help companies improve customer retention.

This project uses Python, SQL, Pandas, NumPy, Matplotlib, Seaborn, and SQLite to clean, analyze, and visualize customer data.

## 🎯 Project Objectives

* Analyze customer churn and retention rates.
* Identify churn patterns across subscription plans.
* Analyze customer complaints and support escalations.
* Calculate average revenue per user (ARPU).
* Measure customer tenure and revenue at risk.
* Explore relationships between customer attributes and churn.
* Create visualizations to communicate business insights.

## 🛠️ Technologies Used

* **Python** — Data analysis and processing
* **Pandas** — Data manipulation and cleaning
* **NumPy** — Numerical computations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **SQL** — Data querying and analysis
* **SQLite** — Database management
* **Jupyter Notebook** — Interactive coding and analysis
* **OpenPyXL** — Reading Excel files

## 📂 Project Files

| File                           | Description                           |
| ------------------------------ | ------------------------------------- |
| `churn_analysis.ipynb`         | Main notebook containing the analysis |
| `customer_churn.db`            | SQLite database                       |
| `customer_churn_data_raw.xlsx` | Raw customer dataset                  |
| `requirements.txt`             | Required Python packages              |
| `README.md`                    | Project documentation                 |

## 🔄 Project Workflow

### 1. Data Import

* Import customer data from Excel and SQLite.
* Load database tables into Pandas DataFrames.
* Inspect database tables and columns.

### 2. Data Cleaning

* Rename columns.
* Remove unnecessary columns.
* Handle missing values.
* Standardize categorical values.
* Convert columns to appropriate data types.
* Clean and prepare customer, subscription, and support data.

### 3. Feature Engineering

* Create a churn flag using cancellation dates.
* Merge customer and support datasets.
* Prepare data for analysis.
* Export processed data when required.

### 4. Exploratory Data Analysis

Analyze important customer metrics, including:

* Customer churn rate
* Customer retention rate
* Churn by subscription plan
* Churn by geographical location
* Average revenue per user (ARPU)
* Average customer tenure
* Revenue at risk
* Support escalation rate
* Average complaints per user
* Correlation between escalation and churn
* Customer churn risk

### 5. Data Visualization

Create visualizations using Matplotlib and Seaborn, including:

* Monthly churn trends
* Churn rate by subscription plan
* Churn by geographical location
* Correlation heatmaps
* Pair plots
* Categorical comparison plots
* Pivot tables

### 6. SQL Analysis

Use SQLite and SQL queries to explore database tables, retrieve records, and perform data analysis.

## 📈 Key Result

The notebook calculates a **customer churn rate of 28.57%** for the dataset used in the analysis.

This metric represents the proportion of customers classified as churned under the notebook's calculation.

Other analyses explore customer retention, subscription plans, revenue at risk, customer complaints, and support escalations.

## 💻 How to Run the Project

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

### Step 2: Download the Project

Download or clone this repository:

```bash
git clone https://github.com/adi-7275/churn-analysis-project.git
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 3: Open the Project Folder

Open Command Prompt or Terminal and navigate to the project directory.

### Step 4: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

If the requirements file is unavailable or incomplete, install the main libraries using:

```bash
pip install numpy pandas matplotlib seaborn openpyxl sqlite-utils jupyter
```

### Step 5: Launch Jupyter Notebook

Run:

```bash
jupyter notebook
```

### Step 6: Run the Notebook

1. Open `churn_analysis.ipynb`.
2. Execute the cells from top to bottom.
3. Ensure the Excel dataset and SQLite database are in the expected location.
4. Review the tables, calculated metrics, and visualizations.

**Note:** An internet connection is required for the initial download and installation of Python packages. After installation, the project can generally run offline, provided all required files and packages are available locally.

## 💡 Business Value

Customer churn analysis can help businesses:

* Understand customer attrition patterns.
* Identify customer segments with higher churn.
* Evaluate subscription and revenue trends.
* Investigate potential relationships between customer support and churn.
* Develop data-driven customer retention strategies.

These analyses can support business decisions, but identifying correlation alone does not establish the causes of churn.

## 🎓 Skills Demonstrated

* Data cleaning and preprocessing
* Exploratory data analysis (EDA)
* Python programming
* SQL querying
* SQLite database management
* Feature engineering
* Customer analytics
* Statistical visualization
* Business insight generation

## 👨‍💻 Author

**Project:** Customer Churn Analysis and Customer Intelligence

**Author credited in the notebook:** Rishabh Mishra

**GitHub Repository:** https://github.com/adi-7275/churn-analysis-project

## 📄 License

This project repository includes an MIT License. Refer to the `LICENSE` file for the applicable terms.
