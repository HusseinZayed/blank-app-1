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
tab1,tab2 = st.tabs(['scatter','histogram'])

with tab1:
  ################################
  num_col = df.select_dtypes(include='number').columns.to_list()

  ###################################
  col1,col2,col3 = st.columns(3)

  with col1:
    x_col = st.selectbox('Choose the x axis',num_col)

  with col2:
    y_col = st.selectbox('Choose the y axis',num_col)

  with col3:
    color = st.selectbox('Choose the color',df.columns.to_list())

  fig1 = px.scatter(df,x=x_col,y=y_col,color=color)
  st.plotly_chart(fig1)

#########################################
with tab2:
  hist_x = st.selectbox('Choose the tab',num_col)
  fig2 = px.histogram(df,x=hist_x)
  st.plotly_chart(fig2)
