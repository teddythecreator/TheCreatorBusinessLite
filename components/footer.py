import streamlit as st

def render_footer():
    st.markdown(
        """<footer style='background-color:#000000; padding:8px; border-radius:4px; margin-top:24px;'>
          <p style='text-align:center; color:#ffffff; margin:0; font-size:0.8rem;'>
            © 2025 TheCreatorsBusiness – Tu partner en digitalización web e IA
          </p>
        </footer>""",
        unsafe_allow_html=True
    )
