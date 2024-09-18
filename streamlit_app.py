import streamlit as st
st.header('Session State')

text_list = []
# Text input
user_input = st.text_input('Enter some text')

# Buttons
if st.button('Append'):
  text_list.append(user_input)
  

# Display the list
st.write('Text list:',text_list)
