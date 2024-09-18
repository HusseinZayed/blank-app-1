import streamlit as st
import pandas as pd

st.header('file upload app 2')
file = st.file_uploader('upload dataset',type=['csv'])
if file is not None:
  df = pd.read_csv(file)
  st.write(df)

num_row = st.slider('choose num rows',min_value=1,max_value=len(df),step=1)
names_column = st.multiselect('choose names of columns',df.columns.to_list())
if names_column:
  st.write(df[:num_row][names_column])
else:
  st.write(df[:num_row])
