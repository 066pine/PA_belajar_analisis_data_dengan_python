import streamlit as st
import pandas as pd

orders_df = pd.read_csv("dashboard/merged_orders.csv")
orders_products_df = pd.read_csv("dashboard/merged_orders_products.csv")

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: WHITE;'>Dashboard Penjualan E-Commerce🛒</h1>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h2 style='text-align: center; color: WHITE;'>HIGHLIGHTS💡</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transaksi", orders_df['order_id'].nunique())
    col2.metric("Total Pembayaran", f"$ {orders_df['payment_value'].sum():,.2f}")
    col3.metric("Rata-rata Skor Ulasan⭐", f"{orders_df['review_score'].mean():.2f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Kategori Produk dengan Transaksi Terbanyak🧩")
    categorized_sales = orders_products_df.rename(columns={"product_category_name_english": "Product category"})["Product category"].value_counts()
    st.bar_chart(categorized_sales)
    
with col2:
    search_category = st.text_input("Cari kategori produk").strip().lower()
    filtered_categories = categorized_sales[categorized_sales.index.str.lower().str.contains(search_category, na=False)] if search_category else categorized_sales
    st.dataframe(filtered_categories, use_container_width=True)
        
st.markdown("***")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Metode Pembayaran Paling Sering Digunakan oleh Pelanggan💳")
    payment = orders_products_df.rename(columns={"payment_type": "Payment type"})["Payment type"].value_counts()
    st.bar_chart(payment)
    
with col2:
    search_payment = st.text_input("Cari metode pembayaran").strip().lower()
    filtered_payment = payment[payment.index.str.lower().str.contains(search_payment, na=False)] if search_payment else payment
    st.dataframe(filtered_payment, use_container_width=True)
    
st.markdown("***")
