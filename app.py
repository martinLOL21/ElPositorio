import streamlit as st
from PIL import Image

st.title( " Hola!!! mi nombre es Martilin " )

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write ("Facilmente puedo realizar el backend y frontend")
image = Image.open("Foto.jpg")
st.image(image, caption="interfaces multimodales")


texto = st.text_input("Escribe algo", "este es mi texto")
st.write("El texto escrito es", texto)
