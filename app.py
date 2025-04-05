import streamlit as st
import requests

st.set_page_config(page_title="Smart Shopping", page_icon="🛒")

st.title("🧠 Smart Shopping Recommender")
st.markdown("Welcome! Get product recommendations based on your interests.")

user_id = st.selectbox("👤 Select your User ID:", [1, 2, 3])

if st.button("✨ Get Recommendations"):
    try:
        response = requests.get(f"http://127.0.0.1:8000/recommend/{user_id}")
        data = response.json()
        recommendations = data.get("recommendations", [])

        if recommendations:
            st.subheader("🛍️ Products Recommended for You")
            for product in recommendations:
                st.image(product["image_url"], width=150)
                st.markdown(f"**{product['name']}**")
                st.markdown(f"💰 Price: ₹{product['price']}")
                st.markdown("---")
        else:
            st.warning("No recommendations found.")
    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")


