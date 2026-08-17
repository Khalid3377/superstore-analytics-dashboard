# 📊 SuperStore Analytics Dashboard

An interactive, high-performance executive web dashboard and ETL analytics project built for visual sales insights, revenue trends, and region/state level breakdowns.

![SuperStore Dashboard Preview](https://img.shields.io/badge/Status-Live-emerald) ![HTML5](https://img.shields.io/badge/Frontend-HTML5%20%7C%20TailwindCSS%20%7C%20ApexCharts-blue) ![Python](https://img.shields.io/badge/Backend-Python%20%7C%20Streamlit-orange)

## 🌐 Live Web Preview & GitHub Pages
Experience the hosted live dashboard directly via GitHub Pages:
👉 **[SuperStore Analytics Live Dashboard](https://khalid3377.github.io/superstore-analytics-dashboard/)**

---

## ✨ Features

- **⚡ Standalone Interactive Dashboard (`index.html`)**:
  - **KPI Metrics**: Real-time Gross Sales, Total Profits, Profit Margins, Units Sold, and Average Discount rate.
  - **Interactive ApexCharts**:
    - **Category-Wise Sales**: Bar chart visualization of product categories.
    - **Regional Distribution**: Donut chart breaking down sales by region.
    - **Time Series Trend Analysis**: Smooth monthly area chart comparing sales vs profits over time.
    - **Customer Segment Breakdown**: Pie chart showing Consumer, Corporate, and Home Office sales.
    - **Scatter Plot Analysis**: Order-level sales vs profit relationship.
  - **Global Filtering**: Date range sliders/selectors + Region, State, and City cascading filters.
  - **Data Table & CSV Export**: Searchable table displaying raw records with direct filtered CSV export capabilities.

- **🐍 Streamlit Analytics App (`app.py`)**:
  - Python-powered data exploration dashboard using Pandas, Plotly Express, and Streamlit.

---

## 📁 Repository Structure

```
├── index.html        # Interactive HTML5 Executive Dashboard
├── data.js           # Lightweight JSON dataset for instant web dashboard loading
├── app.py            # Streamlit Python dashboard app
├── super.xls         # Raw SuperStore Dataset
├── convert_data.py   # Python script converting dataset to web JSON
└── requirements.txt  # Python dependency specification
```

---

## 🚀 Getting Started Locally

### 1. Web Dashboard (No Installation Required)
Simply open `index.html` in any web browser, or serve it locally:
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000/index.html` in your browser.

### 2. Streamlit Dashboard
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit App
streamlit run app.py
```

---

## 📌 How GitHub Pages Hosting Works

This repository is configured to host `index.html` as the entry page via GitHub Pages. 
To enable hosting:
1. Go to your repository **Settings** on GitHub.
2. Click on **Pages** in the left sidebar.
3. Under **Build and deployment -> Source**, select `Deploy from a branch`.
4. Choose the `main` branch and `/ (root)` folder, then click **Save**.
5. Your live site will be ready at: `https://khalid3377.github.io/superstore-analytics-dashboard/`

---

## 👤 Author
Developed & Maintained by **[Khalid3377](https://github.com/Khalid3377)**