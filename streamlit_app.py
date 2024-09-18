
import streamlit as st

area = st.text_input('Enter the radius')


btn = st.button('show')
if btn:
  st.write(f'The area is {area}')
