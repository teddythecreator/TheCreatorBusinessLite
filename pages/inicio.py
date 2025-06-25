# pages/inicio.py

import streamlit as st

def page_inicio():
    """
    Página de Inicio: presentación y llamada a la acción.
    """
    st.markdown(
        """
        <div style="text-align:center; padding: 40px 0;">
            <h1 style="color:#e90074; font-size:3rem; margin-bottom:0.5rem;">
                Impulsa tu Negocio con IA y Tecnología Web
            </h1>
            <p style="font-size:1.2rem; color:#333; max-width:800px; margin:0 auto;">
                En TheCreatorsBusiness somos tu socio estratégico para transformar tu presencia online. 
                Combinamos diseño, desarrollo y soluciones de inteligencia artificial para que tu proyecto 
                digital destaque, crezca y convierta.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.header("¿Qué encontrarás en esta app?")
    st.markdown(
        """
        - 🚀 **Auditoría SEO Avanzada**  
          Analiza en profundidad tus palabras clave, meta-etiquetas, estructura de enlaces y más.

        - ⚡ **Test de Velocidad**  
          Mide el tiempo de carga real de tu web y recibe recomendaciones para acelerar su rendimiento.

        - 🤖 **Chatbot con IA**  
          Interactúa con un asistente virtual capaz de resolver dudas de tus clientes 24/7.

        - 💰 **Calculadora de Presupuestos**  
          Obtén en segundos un presupuesto personalizado según tus necesidades y alcance.

        - 📊 **Dashboard de Métricas**  
          Visualiza en tiempo real los indicadores clave de tu sitio (tráfico, conversiones, engagement).
        """
    )

    st.markdown("---")

    st.subheader("¿Listo para comenzar?")
    if st.button("🌟 Empezar Ahora"):
        st.info("Selecciona la herramienta que necesites en el menú lateral para arrancar tu análisis.")
