# TalentLens — HR Analytics & Recruitment Intelligence

TalentLens is a data analytics project focused on understanding employee attrition, workforce patterns, and HR decision-making through data.

The project uses Python for data inspection and cleaning, PostgreSQL and SQL for querying and analysis, and Power BI for interactive dashboards.

## Project Objectives

- Analyze employee attrition patterns.
- Explore workforce demographics and job-related factors.
- Identify trends across departments, job roles, and employee tenure.
- Develop SQL-based HR analytics insights.
- Build interactive Power BI dashboards to support data-driven HR decisions.

## Tech Stack

- **Python:** Pandas, data inspection, and data cleaning
- **Database:** PostgreSQL
- **Query Language:** SQL
- **Visualization:** Power BI
- **Version Control:** Git and GitHub

## Dataset

The initial analysis uses the IBM HR Analytics Employee Attrition & Performance dataset.

- [Dataset source — Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Records: 1,470 employees
- Original columns: 35

The dataset is fictional and intended for analytics and learning purposes.

## Current Progress

### Completed
- Inspected the raw employee dataset using Python.
- Checked for duplicate records.
- Standardized column names and text values.
- Validated employee identifiers and attrition values.
- Created age-band and tenure-band categories.
- Exported the cleaned dataset to CSV.

### In Progress
- PostgreSQL installation and database setup.
- SQL analysis of employee attrition.
- Power BI dashboard development.

## Project Structure

```text
TalentLens-HR-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── inspect_data.py
│   └── clean_data.py
├── sql/
├── powerbi/
├── reports/
├── .gitignore
└── README.md
```

## How to Run the Python Scripts

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependency:

   ```bash
   pip install pandas
   ```

4. Download the dataset from Kaggle and place the CSV at:

   `data/raw/employee_attrition.csv`

5. Run the inspection script:

   ```bash
   python src/inspect_data.py
   ```

6. Run the cleaning script:

   ```bash
   python src/clean_data.py
   ```

The cleaned dataset will be generated at `data/processed/hr_employees_clean.csv`.

## Planned Analysis

- Overall employee attrition rate
- Attrition by department and job role
- Relationship between overtime and attrition
- Attrition across age groups and tenure bands
- SQL-based HR metrics
- Interactive Power BI dashboards

## Project Status

This project is actively being developed. SQL analysis and Power BI visualizations will be added as the project progresses.


