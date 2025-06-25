# pages/contacto.py

import streamlit as st

def page_contacto():
    """
    Página de Contacto: formulario con llamado amistoso y datos ampliados.
    """
    st.markdown(
        """
        <div style="padding: 20px; background-color:#f9f9f9; border-radius:8px;">
            <h2 style="color:#e90074;">¿Tienes un proyecto en mente?</h2>
            <p>¡Hablemos! Cuéntanos qué necesitas y te responderemos en menos de 24 horas.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre completo", placeholder="Ej. María Pérez")
            email = st.text_input("Email", placeholder="ejemplo@dominio.com")
        with col2:
            telefono = st.text_input("Teléfono", placeholder="+34 600 123 456")
            servicio = st.selectbox(
                "¿Qué servicio te interesa?",
                ["Desarrollo Web", "WordPress & Divi", "E-Commerce", "Academia Online", "Soluciones de IA", "Otro"]
            )
        mensaje = st.text_area("Mensaje", placeholder="Descripción breve de tu proyecto o consulta...")
        enviado = st.form_submit_button("📩 Enviar Mensaje")

        if enviado:
            st.success("✅ ¡Gracias por tu mensaje! Nos pondremos en contacto contigo muy pronto.")
            st.write("---")
            st.write(f"**Nombre:** {nombre}")
            st.write(f"**Email:** {email}")
            if telefono:
                st.write(f"**Teléfono:** {telefono}")
            st.write(f"**Servicio de interés:** {servicio}")
            st.write(f"**Mensaje:** {mensaje}")

    st.markdown("**También puedes contactarnos directamente en:**")
    st.markdown(
        """
        - 📧 <a href="mailto:contacto@thecreator.business">contacto@thecreator.business</a><br>
        - 📞 +34 965 123 456<br>
        - 🌐 <a href="https://www.thecreator.business" target="_blank">www.thecreator.business</a>
        """,
        unsafe_allow_html=True
    )
