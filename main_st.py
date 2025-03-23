import streamlit as st
# Esta llamada debe ser la primera función de Streamlit en ejecutarse
st.set_page_config(page_title="EzOptions", layout="wide")
import ezoptions_cc

def main():
    #st.title("EzOptions en Streamlit")
    #st.write("Bienvenido a la aplicación.")

    #if st.button("Ejecutar EzOptions"):
    ezoptions_cc.main()
        
if __name__ == '__main__':
    main()
