import streamlit as st
st.header("Session state")

st.session_state.fuirts = []

item = st.text_input('add item')

btn = st.button('add')

if btn:
  session_state.fuirts.append(item)

st.write(fuirts)
