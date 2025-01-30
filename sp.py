import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px
df=pd.read_csv(r"C:\Users\91986\OneDrive\Desktop\Stream\Cleaned_data.csv")
st.title("Laptop Analysis")
st.markdown("Explore the variation of Price with other columns in the dataset.")
#Sidebar
cat_cols=['Company','TypeName','Cpu','Gpu','OpSys']
num_cols=['Ram','Weight','Touchscreen','IPS','ppi']
all_cols=cat_cols + num_cols
selected_col = st.sidebar.selectbox("Select a column to compare",all_cols)
#Plotting 
if selected_col:
    if selected_col in cat_cols:
        #Bar chart
        fig=px.box(df,x=selected_col,y='Price',title=f'Price variation by,{selected_col}')
    else:
        #Scatter plot for numerical columns
        fig=px.scatter(df,x=selected_col,y="Price",trendline="ols",title=f"price vs {selected_col}") 
    st.plotly_chart(fig)       
