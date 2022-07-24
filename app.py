import streamlit as st


st.write("""
# Find largest among 3 given numbers
""")

st.header('User Input Parameters')

num1 = st.number_input('Num1')
num2 = st.number_input('Num2')
num3 = st.number_input('Num3')

greatest_num = max(num1, num2, num3)
st.subheader('the largest number is :')
st.write(greatest_num)
