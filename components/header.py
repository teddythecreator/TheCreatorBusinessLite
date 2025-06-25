import streamlit as st

def render_header():
    st.markdown(
        """<header style='background-color:#e90074; padding:12px; border-radius:4px;'>
          <div style='display:flex; justify-content:space-between; align-items:center;'>
            <h1 style='color:#ffffff; margin:0;'>TheCreatorsBusiness</h1>
            <div style='color:#ffffff; font-size:0.9rem;'>
              📧 contacto@thecreator.business | 📞 +34 965 123 456
            </div>
          </div>
        </header>""",
        unsafe_allow_html=True
    )
