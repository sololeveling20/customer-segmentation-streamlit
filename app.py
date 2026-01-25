import streamlit as st
import pandas as pd
import pickle

# Load model, scaler, and recommendations
with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('top_products_per_cluster.pkl', 'rb') as f:
    top_products = pickle.load(f)

st.title("🛒 Customer Segmentation & Product Recommendation")

st.write(
    "This app segments customers using RFM analysis and "
    "recommends products based on customer behavior."
)

st.divider()

# User input
recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input("Frequency (number of purchases)", min_value=1, value=5)
monetary = st.number_input("Monetary (total spend)", min_value=0.0, value=2000.0)

if st.button("Predict Segment & Recommend Products"):

    input_df = pd.DataFrame({
        'Recency': [recency],
        'Frequency': [frequency],
        'Monetary': [monetary]
    })

    input_scaled = scaler.transform(input_df)
    cluster = int(kmeans.predict(input_scaled)[0])

    labels = {
        0: "Regular Customer",
        1: "High-Value Customer",
        2: "At-Risk Customer"
    }

    st.success(f"🧠 Predicted Segment: **{labels[cluster]}**")

    if cluster == 1:
        st.info("💎 Loyal, frequent, high-spending customer.")
    elif cluster == 0:
        st.info("🙂 Regular customer with moderate engagement.")
    else:
        st.warning("⚠️ Customer at risk of churn.")

    st.subheader("🛍️ Recommended Products")

    recommended = (
        top_products[top_products['Cluster'] == cluster]
        .sort_values('Quantity', ascending=False)
        .head(5)['Description']
        .tolist()
    )

    for product in recommended:
        st.write(f"• {product}")
