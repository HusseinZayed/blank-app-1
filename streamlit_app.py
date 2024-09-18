import streamlit as st
import pandas as pd
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



