import streamlit as st

def render():
    st.title("🚀 Meus Projetos")
    st.write("Abaixo, alguns exemplos de aplicações funcionais:")
    
    tab1, tab2 = st.tabs(["Análise de Dados", "Automação"])

    with tab1:
        st.subheader("Dashboard de Vendas")
        # Aqui você pode colocar código real de Streamlit (gráficos, etc)
        st.bar_chart({"Vendas": [10, 25, 15, 30]})
        
    with tab2:
        st.subheader("Web Scraper")
        st.info("Este projeto automatiza a coleta de preços em sites de e-commerce.")
