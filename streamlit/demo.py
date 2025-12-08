import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from xgboost import XGBRegressor #In the end, I picked the XGBoost model as it is the lighest to load
from pathlib import Path
import dill

path_to_repo = Path('..').resolve()

with open(path_to_repo / 'saves' / 'XGB_regressor.pk', 'rb') as f:
    xgb_best = dill.load(f)

logo = Image.open('Vestiaire-collective-logo.jpg.webp')
st.image(logo)

df_transformed = pd.read_feather(path_to_repo / 'data' / 'df_transformed')

df = pd.read_feather(path_to_repo / 'data' / 'df')

st.title('Price Suggestion Demo')

st.write('Find a similar product to what you want to sell, locate its ID with the tool at the bottom and plug it into the model below.')

st.header('Price Prediction')

st.write(
    'Enter a product ID to view its information '
    'and compare predicted vs. actual price. '
)

selected_id = st.number_input( #User freely inputs values
    'Enter Product ID',
    value=0,
    step=1
)

if st.button('Load Prediction'): #We account for invalid IDs

    row = df_transformed[df_transformed['product_id'] == selected_id]

    if row.empty:
        st.error('No product found with this product ID.')
        st.stop() #Message if the input is invalid

    row = row.iloc[0]

    st.subheader('Product Information')
    st.write(row)

    processed = df[df["product_id"] == selected_id]
    processed_row = processed.iloc[0]

    row_for_model = processed_row.values.reshape(1, -1) #Extract the observation from dataset
    prediction = xgb_best.predict(row_for_model)[0] #Predict with model

    actual_price = row.get('price_usd', None)

    st.subheader('Price Comparison')
    colA, colB = st.columns(2)

    with colA:
        st.metric('Predicted Price', f'${np.exp(prediction):,.2f}')

    with colB:
        st.metric('Actual Price', f'${np.exp(actual_price):,.2f}')

st.header('Product Search')

st.write(
    'Locate your products of interest via these filters.'
)

def get_options(df, column): #Extract unique values from features to be options
    opts = df[column].dropna().unique().tolist() #In our dataset, some categories are NaNs which we remove for presentation purposes
    opts = sorted([str(o) for o in opts])
    return ['None Selected'] + opts #Default value where we do not filter

brand_options = get_options(df_transformed, 'brand_name')
material_options = get_options(df_transformed, 'material_type')
type_options = get_options(df_transformed, 'product_type_normalized')
color_options = get_options(df_transformed, 'product_color')
gender_options = get_options(df_transformed, 'product_gender_target')
season_options = get_options(df_transformed, 'product_season')

col1, col2 = st.columns(2)

with col1:
    brand_choice = st.selectbox("Brand", brand_options)
    material_choice = st.selectbox("Material", material_options)
    type_choice = st.selectbox("Product Type", type_options)

with col2:
    color_choice = st.selectbox('Product Color', color_options)
    gender_choice = st.selectbox('Gender Target', gender_options)
    season_choice = st.selectbox('Season', season_options)

if st.button('Load Products'):

    df_filtered = df_transformed.copy()

    filters = {
        'brand_name': brand_choice,
        'material_type': material_choice,
        'product_type_normalized': type_choice,
        'product_color': color_choice,
        'product_gender_target': gender_choice,
        'product_season': season_choice
    }

    for col, val in filters.items():
        if val != 'None Selected':
            df_filtered = df_filtered[df_filtered[col] == val]

    st.subheader('Filtered Results')

    if df_filtered.empty:
        st.warning('No products match the selected filters.')
    else:
        st.write(df_filtered)
        st.success(f'Found {len(df_filtered):,} matching products.')