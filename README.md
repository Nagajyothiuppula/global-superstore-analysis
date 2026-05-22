# 📊 Global Superstore Sales Analysis (Python Project)

## 🧠 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the Global Superstore dataset to understand sales performance across categories, regions, customers, and products.

The goal is to extract **business insights using Python data analysis techniques**.

---

## 🎯 Objective
- Analyze sales performance across categories and regions
- Identify top-performing products and cities
- Understand customer and segment behavior
- Study monthly sales trends
- Generate meaningful business insights from raw data

---

## 📁 Dataset Description
The dataset includes:

- Order details (Order ID, Order Date, Ship Date)
- Customer information (Customer ID, Name, Segment)
- Location data (City, State, Region, Country)
- Product details (Category, Sub-Category, Product Name)
- Sales values

⚠️ Note: This dataset does not include Profit column, so analysis is based on Sales only.

---

## 🛠 Tools Used
- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📊 Data Cleaning Steps
- Loaded dataset using `pandas.read_excel()`
- Handled date formatting using `dayfirst=True`
- Converted Order Date and Ship Date into datetime format
- Extracted Month column for time-based analysis
- Checked missing values and data consistency

---

## 📈 Key Analysis Performed

### 1. Sales by Category
- Compared Furniture, Office Supplies, and Technology

### 2. Sales by Region
- Identified which region contributes most to sales

### 3. Top 10 Products
- Found highest revenue-generating products

### 4. Monthly Sales Trend
- Analyzed sales performance over time

### 5. Customer Analysis
- Identified number of unique customers and order behavior

---

## 🔍 Key Insights
- Technology category performs strongly in sales
- Certain regions contribute significantly to overall revenue
- A small number of products generate a large portion of sales
- Sales show seasonal fluctuations over time
- Customer base is diverse across regions and segments

---

## 📊 Visualizations Included
- Bar charts for category and product analysis
- Pie chart for regional distribution
- Line chart for monthly sales trend

---

## 🚀 How to Run This Project

1. Clone the repository:
```bash
git clone https://github.com/Nagajyothiuppula/global-superstore-analysis.git