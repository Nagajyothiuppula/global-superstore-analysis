import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Global Superstore Sales Dashboard")

# Load data
df = pd.read_csv("train.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# KPI
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Orders", df['Order ID'].nunique())
col3.metric("Total Customers", df['Customer ID'].nunique())

# Sales by Category
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)
plt.ylabel("Sales")
st.pyplot(fig)

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots()
region_sales.plot(kind="bar", ax=ax)
plt.ylabel("Sales")
st.pyplot(fig)

# Top 10 Cities
st.subheader("Top 10 Cities by Sales")
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
city_sales.plot(kind="bar", ax=ax)
plt.ylabel("Sales")
st.pyplot(fig)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

fig, ax = plt.subplots()
monthly_sales.plot(ax=ax)
plt.ylabel("Sales")
plt.xticks(rotation=45)
st.pyplot(fig)