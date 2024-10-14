import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset desde CSV
data = pd.read_csv('catalogo_features_ar.csv')

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Ajustar el ancho del contenedor para la tabla
st.dataframe(df, width=1200)  # Ajusta el ancho según lo que necesites

# Título estilizado y colores
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Catálogo de Features 📊</h1>", unsafe_allow_html=True)
st.markdown("---")

# Campo de búsqueda con placeholder
search_term = st.text_input('🔍 Buscar por nombre o descripción', placeholder='Introduce un término de búsqueda...')

# Filtrar el catálogo por el término de búsqueda
if search_term:
    df_filtrado = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    st.markdown(f"<h3 style='color: blue;'>Mostrando resultados para: {search_term}</h3>", unsafe_allow_html=True)
else:
    df_filtrado = df

# Mostrar el DataFrame filtrado
st.write(df_filtrado)

# Filtro por categoría de features con un título estilizado
st.markdown("<h3 style='color: #4CAF50;'>📂 Filtrar por categoría de features</h3>", unsafe_allow_html=True)
categoria_seleccionada = st.selectbox('Selecciona una categoría:', df['categoria_features'].unique())

# Filtrar el DataFrame por la categoría seleccionada
df_categoria = df[df['categoria_features'] == categoria_seleccionada]

# Mostrar el DataFrame filtrado por categoría
st.write(df_categoria)

# Agregar la opción de descargar el DataFrame filtrado como CSV
@st.cache_data
def convertir_a_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convertir_a_csv(df_filtrado)
st.download_button(label="📥 Descargar datos filtrados como CSV", data=csv, file_name='features_filtrados.csv', mime='text/csv')

# Separador
st.markdown("---")

# Graficar la distribución de recomendaciones
st.markdown("<h3 style='color: #4CAF50;'>📊 Distribución de Recomendaciones</h3>", unsafe_allow_html=True)
counts = df['recomendacion'].value_counts()

# Usar Seaborn para una mejor visualización
fig, ax = plt.subplots()
sns.barplot(x=counts.index, y=counts.values, palette="Blues_d", ax=ax)
ax.set_title('Distribución de Recomendaciones')
ax.set_xlabel('Recomendación')
ax.set_ylabel('Cantidad')
st.pyplot(fig)

# Agregar colores adicionales
st.markdown("<h3 style='color: #FF6347;'>Estadísticas del Catálogo</h3>", unsafe_allow_html=True)
st.write(f"Total de features en el catálogo: {df.shape[0]}")
st.write(f"Categorías únicas de features: {df['categoria_features'].nunique()}")

# Gráfico circular de las categorías
st.markdown("<h3 style='color: #4CAF50;'>🎯 Distribución por Categoría</h3>", unsafe_allow_html=True)
category_counts = df['categoria_features'].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=sns.color_palette("coolwarm", len(category_counts)))
ax2.axis('equal')  # Para hacer el gráfico circular
st.pyplot(fig2)

# Footer con estilo
st.markdown("<h5 style='text-align: center; color: gray;'>Desarrollado con ❤️ usando Streamlit</h5>", unsafe_allow_html=True)
