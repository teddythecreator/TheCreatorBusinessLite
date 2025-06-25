import streamlit as st
# from config import check_env
from components.header import render_header
from components.footer import render_footer

from pages.inicio import page_inicio
from pages.servicios import page_servicios
from pages.portafolio import page_portafolio
from pages.contacto import page_contacto

# check_env()

st.set_page_config(
    page_title="TheCreatorsBusiness",
    page_icon="🚀",
    layout="wide"
)

render_header()

st.sidebar.title("Menú")
pages = {
    "Inicio": page_inicio,
    "Servicios": page_servicios,
    "Portafolio": page_portafolio,
    "Contacto": page_contacto,
}
choice = st.sidebar.radio("Ir a", list(pages.keys()), index=0)
pages[choice]()

render_footer()
