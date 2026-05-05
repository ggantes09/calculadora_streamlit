import streamlit as st
st.title ("Minha calculadora!")

if "historico" not in st.session_state:
    st.session_state.historico = []

numero1 = st.number_input("Digite o primeiro número", step=1)
numero2 = st.number_input("Digite o segundo número", step=1)
operacao = st.selectbox(
        "Selecione os sinais:",
        ("+", "-", "/", "*")
    )

if st.button("Calcular"):
    if operacao == "+":
        resultado = numero1 + numero2
        st.session_state.historico.append (f"{numero1} + {numero2} = {resultado}")
        st.write(resultado)
    elif operacao == "-":
        resultado = numero1 - numero2
        st.session_state.historico.append (f"{numero1} - {numero2} = {resultado}")
        st.write(resultado)
    elif operacao == "/":
        if numero2 == 0:
            st.error("Não é possível dividir por 0!")
        else:
            resultado = numero1 / numero2
            st.session_state.historico.append (f"{numero1} / {numero2} = {resultado}")
            st.write(resultado)
    elif operacao == "*":
        resultado = numero1 * numero2
        st.session_state.historico.append (f"{numero1} * {numero2} = {resultado}")
        st.write(resultado)   
st.subheader("Histórico de Cálculos")
for calculo in st.session_state.historico:
        st.write(calculo)