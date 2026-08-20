import streamlit as st
from PIL import Image

st.title( " Hola!!! mi nombre es Martilin " )

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write ("Facilmente puedo realizar el backend y frontend")
image = Image.open("Foto.jpg")
st.image(image, caption="interfaces multimodales")


texto = st.text_input("Escribe algo", "este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")
