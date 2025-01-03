import streamlit as st

# Título
st.title("Relatório Médico Gerado pela IA")

# Relatório Médico
st.header("Relatório Médico")
st.text("""
Paciente: João Silva
Data: 03/01/2025

Caro João,

Com base nos dados fornecidos, identificamos os seguintes sintomas principais: 
febre, dor muscular e cansaço extremo. Estes sintomas sugerem um quadro inicial de infecção viral. 
Recomendamos manter repouso, boa hidratação e acompanhamento médico para monitorar a evolução. 
Caso os sintomas persistam ou piorem, procure atendimento imediato.

Atenciosamente,
Equipe Saúde Estética AI
""")

# Infográfico
st.header("Infográfico Visual")
st.image("infografico.png", caption="Cuidados em casos de febre alta")
