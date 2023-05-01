import streamlit as st

st.title('Welcome to BMI Calculator')

weight =st.number_input("Enter your weight (in kgs)")

statusn= st.radio('Select you height format: ', ('cm', 'meter', 'feet'))


