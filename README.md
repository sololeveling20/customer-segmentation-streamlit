# Customer Segmentation & Product Recommendation System

This project analyzes e-commerce transaction data to understand customer purchasing behavior and segment customers using **RFM (Recency, Frequency, Monetary) analysis** combined with **KMeans clustering**. Based on the identified customer segments, a **cluster-based product recommendation system** is developed to suggest relevant products. The solution is deployed using a **Streamlit web application** for real-time customer segment prediction and product recommendations.

---

## 📌 Problem Statement
E-commerce platforms generate large volumes of transaction data daily. Analyzing this data is crucial for identifying meaningful customer segments and recommending relevant products to improve customer experience, retention, and revenue. This project aims to leverage unsupervised machine learning techniques to extract actionable insights from retail transaction data.

---

## 🔍 Key Features
- Data cleaning and preprocessing of retail transaction data  
- RFM (Recency, Frequency, Monetary) feature engineering  
- Customer segmentation using KMeans clustering  
- Optimal cluster selection using Elbow Method and Silhouette Score  
- Customer cluster profiling with business insights  
- Cluster-based product recommendation system  
- Interactive Streamlit web application for real-time predictions  

---

## 🧠 Methodology
1. **Data Preprocessing**
   - Removed invalid prices and returns
   - Handled missing values and outliers
   - Created revenue feature

2. **RFM Analysis**
   - Recency: Days since last purchase
   - Frequency: Number of purchases
   - Monetary: Total spending

3. **Clustering**
   - Standardized RFM features
   - Applied KMeans clustering
   - Selected optimal number of clusters using Elbow Method

4. **Product Recommendation**
   - Merged customer clusters with transaction data
   - Identified top-selling products per cluster
   - Recommended products based on cluster popularity

5. **Deployment**
   - Built a Streamlit web application for real-time predictions
   - Loaded trained models and recommendation data for inference

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Matplotlib, Seaborn**
- **Streamlit**

---

## 🚀 How to Run the Application Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/customer-segmentation-project.git
cd customer-segmentation-project
