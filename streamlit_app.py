import streamlit as st
st.header("Session state")

fuirts = []

item = st.text_input('add item')

btn = st.button('add')

if btn:
  fuirts.append(item)

st.write(fuirts)
