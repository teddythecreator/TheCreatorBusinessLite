import streamlit as st

def page_portafolio():
    st.title("Portafolio Destacado 🖼️")
    st.write("Ejemplos de proyectos en Alicante, Murcia y Valencia:")
    st.markdown("---")
    proyectos = [
        {"img":"https://via.placeholder.com/400x250?text=Web+Corporativa","t":"Web Corporativa","loc":"Alicante"},
        {"img":"https://via.placeholder.com/400x250?text=eCommerce","t":"Tienda eCommerce","loc":"Valencia"},
        {"img":"https://via.placeholder.com/400x250?text=Academia","t":"Plataforma e-Learning","loc":"Murcia"},
        {"img":"https://via.placeholder.com/400x250?text=Chatbot+IA","t":"Chatbot IA","loc":"Alicante"},
    ]
    cols = st.columns(2, gap="large")
    for i,p in enumerate(proyectos):
        with cols[i%2]:
            st.image(p["img"], caption=f"{p['t']} ({p['loc']})")
            st.write(f"**{p['t']}** — {p['loc']}")
    st.markdown("¡Más proyectos en camino! 🚀")
