import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

logo = Image.open('Vestiaire-collective-logo.jpg.webp')
st.image(logo)

st.title('User Pricing Guide')

tab1, tab2 = st.tabs(["Product Info", "Seller Info"])

with tab1:
    st.header("Product Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        product_type = st.selectbox("Product Type", 
                                    ["", "Clothing", "Shoes", "Accessories", "Bags", "Other"],
                                    key="product_type")
        product_name = st.text_input("Product Name", key="product_name")
        product_description = st.text_area("Product Description", key="product_description")
        product_keywords = st.text_input("Product Keywords", key="product_keywords")
        product_gender_target = st.selectbox("Gender Target", 
                                            ["", "Women", "Men", "Unisex", "Kids"],
                                            key="product_gender_target")
        product_category = st.text_input("Product Category", key="product_category")
        product_season = st.selectbox("Product Season", 
                                     ["", "Spring", "Summer", "Fall", "Winter", "All Season"],
                                     key="product_season")
        product_condition = st.selectbox("Product Condition", 
                                        ["", "New with tags", "New without tags", "Very good", "Good", "Satisfactory"],
                                        key="product_condition")
    
    with col2:
        product_like_count = st.number_input("Product Like Count", min_value=0, value=0, key="product_like_count")
        product_material = st.text_input("Product Material", key="product_material")
        product_color = st.text_input("Product Color", key="product_color")
        
        st.subheader("Brand Information")
        
        
    st.subheader("Additional Information")
    col3, col4 = st.columns(2)
    with col3:
        has_cross_border_fees = st.checkbox("Has Cross Border Fees", key="has_cross_border_fees")
        warehouse_name = st.text_input("Warehouse Name", key="warehouse_name")

with tab2:
    st.header("Seller Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        seller_username = st.text_input("Seller Username", key="seller_username")
        seller_badge = st.text_input("Seller Badge", key="seller_badge")
        usually_ships_within = st.text_input("Usually Ships Within", key="usually_ships_within")
        seller_country = st.text_input("Seller Country", key="seller_country")
    
    with col2:
        seller_products_sold = st.number_input("Seller Products Sold", min_value=0, value=0, key="seller_products_sold")
        seller_num_products_listed = st.number_input("Seller Number of Products Listed", min_value=0, value=0, key="seller_num_products_listed")
        seller_community_rank = st.number_input("Seller Community Rank", min_value=0.0, value=0.0, key="seller_community_rank")
        seller_num_followers = st.number_input("Seller Number of Followers", min_value=0, value=0, key="seller_num_followers")
        seller_pass_rate = st.number_input("Seller Pass Rate", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="seller_pass_rate")

st.divider()
col1, col2, col3 = st.columns([1, 1, 1])
