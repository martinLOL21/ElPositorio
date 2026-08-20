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

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que Modalidad es la principal en tu interfaz", ("Visual", "Auditivo", "Tactil"))
  if modo == "Visual";
    st.write("La vista es fundamental para tu interfaz")
   if modo == "Auditivo";
    st.write("El audio es fundamental para tu interfaz")
   if modo == "Tactil"
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de Botones")
if st.button("Presiona el boton"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aun")
  
  
