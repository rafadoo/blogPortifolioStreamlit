import streamlit as st

def render():
    st.title("✉️ Vamos construir algo juntos?")
    st.write("Seja para uma consultoria técnica, deploy de infraestrutura ou automação com IA, estou à disposição para ajudar seu negócio a escalar.")

    # Substitua pelo seu e-mail
    seu_email = "rafaeldoo@protonmail.com"

    # Criando o formulário com HTML/CSS para integração com FormSubmit
    contact_form = f"""
    <form action="https://formsubmit.co/{seu_email}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_subject" value="Novo Contato do Portfólio!">
        <input type="text" name="name" placeholder="Seu nome completo" style="width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #333; border-radius: 8px; background-color: #1a1a1a; color: white;" required>
        <input type="email" name="email" placeholder="Seu melhor e-mail" style="width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #333; border-radius: 8px; background-color: #1a1a1a; color: white;" required>
        <select name="service" style="width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #333; border-radius: 8px; background-color: #1a1a1a; color: white;">
            <option value="Consultoria IA/RAG">Consultoria IA / RAG</option>
            <option value="Automação n8n">Automação de Workflows (n8n)</option>
            <option value="Infraestrutura Docker/Linux">Infraestrutura Docker / Linux</option>
            <option value="Odoo ERP">Implementação Odoo ERP</option>
            <option value="Consultoria para soluções em TI em geral">Implementação Odoo ERP</option>
            <option value="Outros">Outros Assuntos</option>
        </select>
        <textarea name="message" placeholder="Como posso ajudar o seu projeto?" style="width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #333; border-radius: 8px; background-color: #1a1a1a; color: white; min-height: 150px;" required></textarea>
        <button type="submit" style="background-color: #00d4ff; color: #1a1a1a; padding: 12px 20px; border: none; border-radius: 8px; cursor: pointer; width: 100%; font-weight: bold; font-size: 16px;">Enviar Proposta</button>
    </form>
    """

    col_form, col_info = st.columns([1.5, 1], gap="large")

    with col_form:
        st.markdown("### Envie uma mensagem")
        # Renderiza o formulário HTML
        st.markdown(contact_form, unsafe_allow_html=True)

    with col_info:
        st.markdown("### Canais Oficiais")
        st.write("Prefere uma conversa direta?")
        
        # Botões de link personalizados com estilo de marca
        st.link_button("🤝 Agendar Reunião (Calendly)", "https://calendly.com/rafaeldooubuntu", use_container_width=True)
        st.link_button("🔗 Conectar no LinkedIn", "https://linkedin.com/in/seu-usuario", use_container_width=True)
        st.link_button("💻 Portfólio no GitHub", "https://github.com/rafadoo/", use_container_width=True)
        
        st.divider()
        
        st.markdown("### 🕒 Horário de Atendimento")
        st.caption("Segunda a Sexta: 09h às 18h")
        st.caption("Resposta média: Menos de 24 horas")

    st.divider()
    st.info("💡 **Dica de Negócio:** Se você busca uma automação específica ou integração com ERP, mencione as ferramentas que já utiliza para agilizarmos o diagnóstico.")
