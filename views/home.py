import streamlit as st

def render():
    # 1. Headline de Impacto
    st.title("Especialista em Infraestrutura de TI")
    st.subheader("Transformando tecnologia livre em eficiência operacional para o seu negócio.")

    st.markdown("---")

    # 2. Layout Principal (Quem sou eu + Foto)
    col_foto, col_bio = st.columns([1, 2], gap="large")
    
    with col_foto:
        # Foto de perfil com borda arredondada via CSS se desejar
        st.image("https://avatars.githubusercontent.com/u/83986662?s=400&u=809fac95aa11dce87070ac2d071c955d63d5fb86&v=4", width=280)
        st.markdown("### 📍 Localização")
        st.write("São Paulo, Brasil")

    with col_bio:
        st.markdown("""
        ### Proposta de Valor
        Ajudo empresas e pessoas a escalarem suas operações com tecnologias **Open Source**, eliminando custos e garantindo total soberania sobre seus dados.
        
        Com mais de 10 anos de atuação em TI e sólida experiência em **Linux** e ecossistemas **Python**, projeto infraestruturas robustas que integram desde a inovação da IA generativa à estabilidade de ERPs modernos.
        """)
        
        # Botão de destaque para conversão rápida
        st.link_button("Solicitar Orçamento de Projeto", "https://calendly.com/rafaeldooubuntu")

    st.markdown("---")

    # 3. Pilares de Atuação (Escalabilidade e Visão de Negócio)
    st.header("Soluções Estratégicas")
    
    # Criando 3 colunas para serviços
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### 🤖 IA & RAG")
        st.write("Implementação de LLMs locais com contexto de documentos (Llama/LangChain) para automação de conhecimento.")
        
    with c2:
        st.markdown("#### 📦 ERP & Gestão")
        st.write("Deploy e customização de Odoo ERP para centralizar vendas, estoque e financeiro em uma única plataforma.")
        
    with c3:
        st.markdown("#### ⚙️ Automação (n8n)")
        st.write("Integração de APIs e fluxos de trabalho que economizam centenas de horas manuais mensalmente.")

    st.markdown("---")

    # 4. A Prova Técnica (Stack de Infraestrutura)
    st.header("🛠️ Stack de Infraestrutura & Confiança")
    
    col_infra, col_db = st.columns(2)
    
    with col_infra:
        st.markdown("##### 🐳 DevOps & OS")
        st.info("""
        - **OS:** Linux (Ubuntu/Debian)
        - **Containers:** Docker & Docker Compose
        - **Cloud:** Nextcloud & Self-Hosting
        """)

    with col_db:
        st.markdown("##### 📊 Bancos de Dados")
        st.success("""
        - **Relacionais:** PostgreSQL, MySQL, Firebird, MSSQL
        - **Vetoriais:** ChromaDB / Pinecone (IA)
        - **NoSQL:** MongoDB
        """)

    # 5. Frase de Fechamento Profissional
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("💡 **Diferencial:** Todos os projetos são entregues com documentação técnica e containers prontos para produção, além do suporte humanizado.")
