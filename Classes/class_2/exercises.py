#calculadora

import streamlit as st
st.title('Calculadora')

number_1 = st.number_input('first number: ')
number_2 = st.number_input('second number: ')

if st.button('RESULTADO SOMA'):
    soma = number_1 + number_2
    st.success(soma)

#calculadora imc

import streamlit as st
st.title('Calculadora de IMC')

weight = st.number_input('weight: ')
height = st.number_input('height: ')

if st.button('RESULTADO IMC'):
    imc = weight / (height ** 2)
    st.success(imc)

#calculadora imc

import streamlit as st
st.title('Conversor de temperatura')

celsius = st.number_input('Degrees in Celsius: ')

if st.button('Convert Celsius to Fahrenheit'):
    celsius_fahrenheit = (celsius*1.8)+32
    st.success(celsius_fahrenheit)

# password generator

