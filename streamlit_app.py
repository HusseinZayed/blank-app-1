## example 1 with sidebar and spinner
import streamlit as st

import time
st.sidebar.title('Sidebar')

st.header('Calculate Area')

with st.sidebar:
  choose = st.selectbox('Choose the shape',['Circle','Rectangle'])

area =None

if choose == 'Circle':
  r = st.number_input('Enter the radius',min_value=1,max_value=50)
  area = r*r*3.14
elif choose == 'Rectangle':
  l = st.number_input('Enter the length',min_value=1,max_value=50)
  w = st.number_input('Enter the width',min_value=1,max_value=50)
  area = l*w

btn = st.button('Calculate')
if btn:
  with st.spinner('Calculating...'):
    time.sleep(2)
  st.write(f'The area is {area}')
