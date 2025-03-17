import streamlit as st
import requests
from bs4 import BeautifulSoup

def analizar_xml():
    st.title("Análisis XML de Starbucks en México")

    # URL del archivo XML
    url = "https://raw.githubusercontent.com/DaTolok/python-edx/main/Modulo%203/startbucks_mexico.xml"
    response = requests.get(url)
    xml_content = response.text

    # Procesar con BeautifulSoup y lxml
    soup = BeautifulSoup(xml_content, "lxml-xml")

    # Obtener todos los resultados
    results = soup.find_all("result")
    num_results = len(results)

    # Extraer el primer resultado y sus elementos hijos
    first_result = results[0]
    child_elements = [child.name for child in first_result.find_all(recursive=False)]

    # Obtener valores únicos de la etiqueta "types"
    unique_types = set(tag.text for result in results for tag in result.find_all("type"))

    # Obtener todas las calificaciones y calcular máximo/mínimo
    ratings = [float(result.find("rating").text) for result in results if result.find("rating")]
    max_rating = max(ratings)
    min_rating = min(ratings)

    # Identificar el Starbucks con el rating más alto
    best_starbucks = next(result for result in results if float(result.find("rating").text) == max_rating)

    # Extraer el estado del Starbucks con mejor rating
    formatted_address = best_starbucks.find("formatted_address").text
    state = formatted_address.split(",")[-2].strip()

    # Mostrar resultados en Streamlit
    st.write(f"**Número total de resultados:** {num_results}")
    st.write(f"**Elementos hijos inmediatos del primer resultado:** {len(child_elements)}")
    st.write(f"**Valores únicos en 'types':** {unique_types}")
    st.write(f"**Valor máximo de rating:** {max_rating}")
    st.write(f"**Valor mínimo de rating:** {min_rating}")
    st.write(f"**El Starbucks con mayor rating está en:** {state}")

if __name__ == "__main__":
    analizar_xml()
