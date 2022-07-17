import streamlit as st

# Two lists of sentences
sentences1 = st.text_input('Insert sentences 1:')


sentences2 = st.text_input('Insert sentences 2:')



if st.button('Submit'):
  st.write('sentences1 is: ', sentences1)
  st.write('sentences2 is: ', sentences2)

