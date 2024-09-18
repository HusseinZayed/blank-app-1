## add filter and divid it as columns

import streamlit as st
import pandas as pd
import plotly.express as px

st.header('File Upload')
uploaded_file = st.file_uploader('Choose a file',type=['csv'])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

n_rows = st.slider('Enter the number of rows',min_value=1,max_value=len(df),step=1)
column_choose = st.multiselect('Choose the columns',df.columns.to_list())

if column_choose:
  st.write(df[:n_rows][column_choose])
else:
  st.write(df[:n_rows])
  
################################

num_col = df.select_dtypes(include='number').columns.to_list()

x_col = st.selectbox('Choose the x axis',num_col)
y_col = st.selectbox('Choose the y axis',num_col)
color = st.selectbox('Choose the color',df.columns.to_list())

fig1 = px.scatter(df,x=x_col,y=y_col,color='red')
st.plotly_chart(fig1)
