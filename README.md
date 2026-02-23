# Rafael do Ó - Portfolio & Infra Solutions

Bem-vindo ao meu ecossistema digital. Este projeto é mais do que um portfólio; é uma demonstração ativa de arquitetura **Open Source**, **IA Generativa** e **Infraestrutura Escalável**.

O site é construído em **Python** e opera de forma modular para facilitar a manutenção e a integração de novas soluções de negócio.

## 🌐 Live Demo
[Acesse meu portfólio aqui](https://rafaeldo-infra.streamlit.app)

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Frontend/UI:** Streamlit & Streamlit Option Menu
- **Infraestrutura:** Docker & Docker Compose (Self-hosted em ambiente Linux)
- **Integrações:** FastAPI, LangChain (RAG), n8n, Odoo ERP
- **Bancos de Dados:** PostgreSQL, MSSQL, Firebird, MongoDB, ChromaDB (Vector)

## 📁 Estrutura do Projeto
```text
├── streamlitApp.py        # Orquestrador principal e layout
├── requirements.txt       # Dependências do sistema
├── views/                 # Módulos independentes por página
│   ├── home.py            # Proposta de valor e bio
│   ├── portfolio.py       # Showcase de projetos e infra
│   ├── blog.py            # Motor de renderização automática de posts
│   └── contato.py         # Formulário de conversão de negócios
└── posts/                 # Artigos em Markdown (.md)
