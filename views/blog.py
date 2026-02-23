import streamlit as st
import os

def render():
    st.title("📝 Insights & Tecnologia")
    st.markdown("""
        Explorando o ecossistema **Open Source**, **IA** e **Infraestrutura**. 
        Aqui compartilho visões técnicas e estratégicas para negócios.
    """)
    st.divider()

    posts_dir = "posts"

    if not os.path.exists(posts_dir):
        st.error("Repositório de artigos não configurado.")
        return

    files = [f for f in os.listdir(posts_dir) if f.endswith(".md")]
    files.sort(reverse=True) # Mantém os mais recentes no topo

    if not files:
        st.info("Preparando conteúdo exclusivo. Volte em breve!")
        return

    for file in files:
        file_path = os.path.join(posts_dir, file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                conteudo = f.read()
                linhas = conteudo.split('\n')
                
                # Melhoria: busca o primeiro H1 (#) para o título
                titulo_artigo = "Artigo Sem Título"
                for linha in linhas:
                    if linha.startswith('# '):
                        titulo_artigo = linha.replace('# ', '')
                        break
                
                with st.container():
                    # Layout estilo card
                    with st.expander(f"📄 {titulo_artigo}"):
                        st.markdown(conteudo)
                        st.caption(f"📅 Publicado em: {file[:10]}") # Assume formato YYYY-MM-DD-nome.md
                    st.markdown("<br>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Erro ao carregar o artigo {file}.")

# Dica: Nomeie seus arquivos como '2026-02-23-meu-post.md' para ordenação automática.
