import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset desde CSV
data = pd.read_csv('catalogo_features_ar.csv')

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Ajustar el ancho del contenedor para la tabla

# Título estilizado y colores
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Catálogo de Features 📊</h1>", unsafe_allow_html=True)
st.markdown("---")

# Campo de búsqueda con placeholder
search_term = st.text_input('🔍 Buscar por nombre o descripción', placeholder='Introduce un término de búsqueda...')

# Filtrar el catálogo por el término de búsqueda
if search_term:
    df_filtrado = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    # Mostrar cuántos features coinciden con la búsqueda y de qué categorías son
    count_by_category = df_filtrado['categoria_features'].value_counts()
    st.markdown(f"<h3 style='color: blue;'>Mostrando {df_filtrado.shape[0]} resultados para: {search_term}</h3>", unsafe_allow_html=True)
    st.write(f"Distribución de categorías en los resultados:")
    st.write(count_by_category)

    # Contar cuántos features tienen un valor no vacío en la columna "duplicados"
    #duplicados_count = df_filtrado[df_filtrado['duplicados'] != ""].shape[0]
    
    # Mostrar el número de features duplicados encontrados
    #st.markdown(f"<h3 style='color: red;'>Features duplicados en los resultados filtrados: {duplicados_count}</h3>", unsafe_allow_html=True)
else:
    df_filtrado = df


    
# Mostrar el DataFrame filtrado
st.dataframe(df_filtrado) 

# Agregar la opción de descargar el DataFrame filtrado como CSV
@st.cache_data
def convertir_a_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convertir_a_csv(df_filtrado)
st.download_button(label="📥 Descargar datos filtrados como CSV", data=csv, file_name='features_filtrados.csv', mime='text/csv')

# Separador
st.markdown("---")



# Gráfico circular de las categorías
st.markdown("<h3 style='color: #4CAF50;'>🎯 Distribución por Categoría</h3>", unsafe_allow_html=True)
category_counts = df['categoria_features'].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=sns.color_palette("coolwarm", len(category_counts)))
ax2.axis('equal')  # Para hacer el gráfico circular
st.pyplot(fig2)

# Footer con estilo
st.markdown("<h5 style='text-align: center; color: gray;'>Desarrollado con ❤️ usando Streamlit</h5>", unsafe_allow_html=True)
