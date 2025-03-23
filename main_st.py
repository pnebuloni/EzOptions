import streamlit as st
import ezoptions_cc

st.title("EzOptions en Streamlit Community Cloud")
st.write("Presiona el botón para ejecutar la lógica principal.")

if st.button("Ejecutar EzOptions"):
    st.info("Ejecutando la lógica principal de EzOptions...")
    ezoptions_cc.main()
    st.success("Proceso completado.")

