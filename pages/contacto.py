import streamlit as st

def page_contacto():
    st.title("Contáctanos 📧")
    st.write("Déjanos tu mensaje y te responderemos pronto:")
    st.markdown("---")
    with st.form("contact_form", clear_on_submit=True):
        n = st.text_input("Nombre")
        e = st.text_input("Email")
        m = st.text_area("Mensaje")
        ok = st.form_submit_button("Enviar")
        if ok:
            st.success("✅ ¡Mensaje enviado!")
            st.write(f"**Nombre:** {n}")
            st.write(f"**Email:** {e}")
            st.write(f"**Mensaje:** {m}")
