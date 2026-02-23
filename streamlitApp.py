import streamlit as st
from streamlit_option_menu import option_menu
from views import home, blog, portfolio, contato

# 1. Configuração da página (Defina o favicon com um emoji ou link)
st.set_page_config(page_title="Rafael do Ó", page_icon="", layout="wide")

# --- CSS BLINDADO ---
st.markdown("""
    <style>
        /* 1. Garante que o container principal tenha espaço para o menu e sidebar */
        .block-container {
            padding-top: 4rem !important; 
            padding-bottom: 1rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }

        /* 2. Mantém o header tecnicamente visível mas visualmente transparente */
        /* Isso impede que a sidebar suma ou o menu seja cortado */
        header[data-testid="stHeader"] {
            background: rgba(0,0,0,0);
            height: 3rem;
        }

        /* 3. Estilização do botão da sidebar para garantir visibilidade */
        button[kind="header"] {
            background-color: transparent;
            color: #00d4ff !important;
        }

        /* 4. Remove elementos desnecessários sem quebrar o layout */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* 5. Ajuste fino para o Option Menu não colar no topo */
        .nav-link {
            padding: 8px 20px !important;
        }
        
        /* Responsividade para telas menores */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Sempre carregada antes do menu para garantir o estado) ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/83986662?s=400&u=809fac95aa11dce87070ac2d071c955d63d5fb86&v=", width=100) 
    st.markdown("### Rafael do Ó")
    st.caption("Especialista em Open Source & IA")
    st.markdown("---")
    
    st.success("**Parcerias e Negócios**")
    st.link_button("📅 Agendar Consultoria", "https://calendly.com/rafaeldooubuntu")
    
    st.markdown("---")
    st.markdown("🌐 **Status da Infra**")
    # 
    st.markdown("🟢 `Servidor Linux: Online`")
    st.markdown("🟢 `FastAPI RAG: Operacional`")
    st.markdown("🟢 `Docker Containers: 12 Active`")

# --- MENU SUPERIOR ---
# Envolvido em um container para isolamento total
with st.container():
    selected = option_menu(
        menu_title=None, 
        options=["Início", "Blog", "Portfólio", "Contato"], 
        icons=["house", "journal-text", "code-square", "envelope"], 
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#1a1a1a", 
                "border-radius": "8px",
                "margin-bottom": "20px"
            },
            "icon": {"color": "#00d4ff", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "15px", 
                "color": "white",
                "text-transform": "uppercase"
            },
            "nav-link-selected": {
                "background-color": "#262626", 
                "border-bottom": "3px solid #00d4ff",
                "font-weight": "bold"
            },
        }
    )

# --- ROTEAMENTO ---
views_dict = {
    "Início": home.render,
    "Blog": blog.render,
    "Portfólio": portfolio.render,
    "Contato": contato.render
}

# Execução da View
if selected in views_dict:
    # Encapsulamos a renderização em um div para controle de layout se necessário
    with st.container():
        views_dict[selected]()
    
# --- RODAPÉ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
col_f1, col_f2 = st.columns([3, 1])
with col_f1:
    st.caption("© 2026 Rafael do Ó - Consultoria em Infraestrutura Open Source & IA")
with col_f2:
    st.caption("Powered by Python & Docker")
