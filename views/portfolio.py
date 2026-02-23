import streamlit as st

def render():
    st.title("Soluções Corporativas & Ecossistema Open Source")
    st.markdown("""
        Minhas soluções são focadas na **soberania de dados** e na **eficiência operacional**. 
        Utilizo ferramentas de código aberto para entregar performance de nível empresarial sem custos de licenciamento abusivos.
    """)
    st.divider()

    # --- SEÇÃO 1: IA & INTELIGÊNCIA DE DADOS ---
    st.header("🤖 Inteligência Artificial Generativa")
    
    col_ai_txt, col_ai_img = st.columns([2, 1])
    
    with col_ai_txt:
        st.subheader("RAG Chatbot: Inteligência sobre Documentos")
        st.write("""
            Desenvolvi uma arquitetura de **Retrieval-Augmented Generation (RAG)** que permite consultar 
            conhecimento interno de forma privada e segura.
            
            - **Caso de Uso:** Consultas em manuais técnicos, bases jurídicas ou documentação interna.
            - **Segurança:** Implementado com modelos locais (Llama 3), garantindo que os dados nunca saiam da sua infraestrutura.
        """)
        st.code("Stack: Llama 3, LangChain, FastAPI, ChromaDB (Vector DB), Docker", language="python")
    
    with col_ai_img:
        # Espaço para uma imagem ilustrativa ou ícone de IA
        st.info("💡 **Diferencial:** Integração total via API com sistemas legados (Firebird/MSSQL).")

    st.divider()

    # --- SEÇÃO 2: INFRAESTRUTURA & ERP ---
    st.header("🐳 Infraestrutura & Gestão (Self-Hosted)")
    st.write("Especialista em orquestração de serviços críticos via Docker.")

    tab1, tab2, tab3 = st.tabs(["⚙️ Automação (n8n)", "📦 ERP (Odoo)", "☁️ Nuvem Privada"])

    with tab1:
        st.subheader("Orquestração de Workflows com n8n")
        st.write("""
            Automação de processos entre diferentes plataformas (CRM, E-mail, Banco de Dados e WhatsApp).
            - **Impacto:** Redução de erros manuais e integração em tempo real entre sistemas que não se comunicam nativamente.
        """)
        st.link_button("Ver fluxo de exemplo no GitHub", "https://github.com/rafaeldooubuntu")

    with tab2:
        st.subheader("Gestão Integrada com Odoo")
        st.write("""
            Implementação e customização do Odoo ERP para controle total de vendas, estoque e financeiro.
            - **Expertise:** Migração de dados de bancos legados para o ecossistema Odoo.
        """)

    with tab3:
        st.subheader("Nextcloud: Sua Nuvem, Suas Regras")
        st.write("""
            Alternativa profissional ao Google Drive/Dropbox. Armazenamento seguro, calendários e colaboração 
            de documentos em tempo real dentro do seu próprio servidor.
        """)

    st.divider()

    # --- SEÇÃO 3: EXPERTISE EM BANCO DE DADOS ---
    st.header("📊 Inteligência em Bancos de Dados")
    st.write("Sólida experiência em arquiteturas relacionais e modernas para suporte à decisão.")
    
    # Grid de Bancos de Dados
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Relacionais", "PostgreSQL/MSSQL")
    c2.metric("Legados", "Firebird")
    c3.metric("NoSQL", "MongoDB")
    c4.metric("Vetoriais", "ChromaDB")

    # --- CHAMADA PARA AÇÃO (CTA) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("🎯 **Precisa de uma solução personalizada?** Estou pronto para projetar a arquitetura ideal para sua necessidade.")
