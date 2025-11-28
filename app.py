import pandas as pd
import plotly.express as px
import streamlit as st
        
# 1. Leemos los datos (el libro de coches)
car_data = pd.read_csv('vehicles_us.csv') 

# 2. Ponemos un Título bonito
st.header('¡Mi Panel de Control de Coches! 🚗💨')

# 3. Creamos un botón mágico
boton_histograma = st.button('Construir histograma') # Botón 1
        
if boton_histograma: # Si alguien aprieta el botón 1
    st.write('¡Mira cuántos kilómetros tienen estos coches!')
            
    # Crear el dibujo
    fig = px.histogram(car_data, x="odometer")
        
    # Mostrar el dibujo
    st.plotly_chart(fig, use_container_width=True)

# 4. Creamos otro botón (o una casilla de verificación si eres valiente)
boton_dispersion = st.button('Construir gráfico de dispersión') # Botón 2

if boton_dispersion: # Si aprietan el botón 2
    st.write('Comparando precio vs. año')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
    