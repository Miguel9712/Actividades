import streamlit as st
# ------------------------------
#  STREAMLIT MULTIPÁGINA
# ------------------------------
def home():
    st.title("Inicio")
    st.write("Hellou")

def page1():
    st.title("Página 1")
    st.write("Esta es la primera página.")

def page2():
    st.title("Página 2")
    st.write("Esta es la segunda página.")

# ------------------------------
# SECCIÓN PRINCIPAL DE LA APP
# ------------------------------
def main():
    st.sidebar.title("Navegación")
    pages = {
        "Inicio": home,
        "Página 1": page1,
        "Página 2": page2,
    }
    
    choice = st.sidebar.radio("Ir a:", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()