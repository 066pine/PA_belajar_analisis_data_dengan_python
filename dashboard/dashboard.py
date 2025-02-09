import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

orders_products_df = pd.read_csv("dashboard/merged_orders_products.csv")
orders_df = pd.read_csv("dashboard/merged_orders.csv")

    st.title("Dashboard E-Commerce")

    with st.container(border=True):
        st.subheader("Summary highlight")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Pesanan", orders_df['order_id'].nunique())
        col2.metric("Total Pembayaran", f"$ {orders_df['payment_value'].sum():,.2f}")
        col3.metric("Rata-rata Skor Ulasan", f"{orders_df['review_score'].mean():.2f}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Order Trends")
        orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
        df_trend = orders_df.resample('ME', on='order_purchase_timestamp').size()
        fig, ax = plt.subplots()
        df_trend.plot(ax=ax)
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Jumlah Pesanan")
        ax.set_title("Tren Pesanan Bulanan")
        st.pyplot(fig)

    with col2:
        st.subheader("Top Categories")
        fig, ax = plt.subplots()
        orders_products_df['product_category_name_english'].value_counts().head(10).plot(kind='bar', ax=ax)
        ax.set_xlabel("Kategori Produk")
        ax.set_ylabel("Jumlah")
        ax.set_title("Top 10 Kategori Produk")
        plt.xticks(rotation=45)
        st.pyplot(fig)
