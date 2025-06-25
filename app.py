# app.py

import os
import sys

# Fuerza a que Python busque módulos antes en la carpeta actual
# (ahora el directorio donde está este app.py)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
# from config import check_env    # puedes reactivar cuando tengas tu .env
from components.header import render_header
from components.footer import render_footer

# Importa tus páginas (asegúrate de que existen estos archivos en pages/)
from pages.inicio     import page_inicio
from pages.servicios  import page_servicios
from pages.portafolio import page_portafolio
from pages.contacto   import page_contacto

# check_env()   # activa cuando tengas .env completo

# Configuración general
st.set_page_config(
    page_title="TheCreatorsBusiness",
    page_icon="🚀",
    layout="wide"
)

# Header fijo
render_header()

# Menú lateral
st.sidebar.title("Menú")
pages = {
    "Inicio":     page_inicio,
    "Servicios":  page_servicios,
    "Portafolio": page_portafolio,
    "Contacto":   page_contacto,
    # luego podrás añadir más herramientas aquí
}
choice = st.sidebar.radio("Ir a", list(pages.keys()), index=0)

# Render de la página seleccionada
pages[choice]()

# Footer fijo
render_footer()
