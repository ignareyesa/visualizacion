import streamlit as st
import pandas as pd

df = pd.read_csv("airbnb.csv")

st.title("AirBNB Analysis")

## 3º Create a table with the name of the apartment, neighbourhood_group, neighbourhood, price and reviews_per_month

df_select = df[["name", "neighbourhood_group","neighbourhood", "price", "reviews_per_month"]]
st.dataframe(df_select.head(),
    column_config = {
        "name":"Aparment Name",
        "price": st.column_config.NumberColumn(
            label="Price (€)",
            format="€%.2f"
        ),
        "reviews_per_month" : st.column_config.ProgressColumn(
            label = "Notas por mes",
            format = "compact"
        )
    })

## 4º Create a boxplot for the prices for neighbourhood after selecting one neighbourhood group
import plotly.express as px
df_select.dropna(inplace = True) 

neighbourhood = st.sidebar.multiselect("Please, select one neighbourhood",
                                df_select["neighbourhood_group"].unique())

df_select = df_select[df_select["neighbourhood_group"].isin(neighbourhood)] 

df_select = df_select[df_select["price"]<500]
fig = px.box(df_select, x = "neighbourhood", y="price")

## 6º Crete columns
col1, col2 = st.columns(2)
with col1:
    st.text("I am column 1")

with col2: 
    st.text("I am column 1")


## 5º Create a map with all the listings in that neighbourhood



## 6º Create a new tab 





