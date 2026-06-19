# 🏭 Enterprise Supply Chain Data Cleaning & Automation Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A production-ready, data-quality engineering automation pipeline dashboard built to process high-throughput logistics transaction streams. This application ingests complex, anomaly-ridden supply chain datasets, executes deep mathematical cleaning and data alignment operations, and delivers interactive executive-level business intelligence profiles.

---

## 🎯 Project Vision & Core Features

When managing real-world enterprise databases, data is inherently messy. This project acts as a middle-tier extraction and transformation engine to handle data inconsistencies smoothly without breaking down analytical workflows.

### ⚙️ Automated Preprocessing Engines
* **Deduplication Engine:** Evaluates operational snapshot records and drops structural row iterations automatically.
* **Text Harmonization Matrix:** Normalizes varied text cases (e.g., matching `DHL Global` and `dhl global`), strips white-space padding, and standardizes legacy vendor schemas.
* **Outlier Mitigation:** Automatically enforces strict domain constraints, transforming invalid entries (such as negative transit days or missing rows) into clean statistical flags.
* **Multi-Variate Imputation:** Isolates empty property matrices and resolves null records dynamically using statistical column-wise median/mode values.

---

## 📊 Analytics Dashboard Modules

The application translates clean tables into operational awareness via a modern web interface split into modular views:

1. **Executive Data Integrity Analytics:** Instantly displays Key Performance Indicators (KPIs) showing row drops, columns processed, and total resolved null items alongside a direct CSV export trigger.
2. **Pipeline Transformations Panel:** Offers explicit step-by-step console logs tracking the success criteria of every processing phase alongside an interactive pre-processed null cell density heatmap.
3. **Raw Auditing Spreadsheet:** Provides direct table indexing to let auditors observe the data architecture before data treatment cycles began.

---

## 📁 Architecture & Tech Stack

```text
data_cleaning_automation/
│
├── app.py                  # Core Data Engineering Framework & UI Engine
├── README.md               # Portfolio-ready System Documentation
└── venv/                   # Isolated Virtual Environment Sandbox
