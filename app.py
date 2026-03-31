import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("D:/coding/data_ges/Superstore.csv", encoding='latin1')

st.title("Sales Dashboard")

# Total Sales
total_sales = df['Sales'].sum()
st.metric("Total Sales", f"${total_sales:,.2f}")

# Sales per Category
category_sales = df.groupby('Category')['Sales'].sum()

st.subheader("Sales by Category")
fig, ax = plt.subplots()
category_sales.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Top Products
st.subheader("Top 5 Products")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
st.write(top_products)

