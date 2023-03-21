import streamlit as st
import requests

st.title("Informacion de la Estacion Espacial Internacional")

posicion_iss = requests.get("http://api.open-notify.org/iss-now.json")
json_iss = posicion_iss.json()
st.json(json_iss)

st.table(json_iss)

st.write(json_iss["iss_position"]["latitude"])
st.write(json_iss["iss_position"]["longitude"])

posicion = "https:maps.google.com/?q{
