import streamlit as st
st.header("Session state")

st.session_state.fuirts = []

item = st.text_input('add item')

btn = st.button('add')

if btn:
  st.session_state.fuirts.append(item)

st.write(st.session_state.fuirts)
