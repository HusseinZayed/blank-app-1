## add filter and divid it as columns

import streamlit as st
## with session_state
# application1 3
import streamlit as st
st.header('Session State')

if 'text_list' not in st.session_state:
  st.session_state.text_list = []
# Text input
user_input = st.text_input('Enter some text')

# Buttons
if st.button('Append'):
  st.session_state.text_list.append(user_input)
  

# Display the list
st.write('Text list:', st.session_state.text_list)
