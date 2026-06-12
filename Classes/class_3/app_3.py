import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# objetivo: previsão de FATURAMENTO baseado nos investimentos

st.scatter_chart(dados_vendas, x = 'investimento', y= 'faturamento')
modelo_vendas = LinearRegression() 
modelo_vendas.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

investimento = st.slider('Investimento', 0,12,5)
faturamento = modelo_vendas.predict([[investimento]])
print(faturamento)

st.metric(f'Seu faturamento seria' ,f'{min(faturamento[0], 10.0):.1f}')
