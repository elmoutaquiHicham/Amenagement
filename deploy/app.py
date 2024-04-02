import streamlit as st
import pandas as pd

# Chargement des données depuis un fichier CSV (ou une autre source de données)
@st.cache
def load_data():
    # Remplacez 'nom_du_fichier.csv' par le nom de votre fichier CSV contenant les données des bungalows
    return pd.read_excel('deploy/bungalow_tk.xlsx')

# Fonction pour filtrer les références en fonction des valeurs sélectionnées
def filter_references(data, filters):
    filtered_data = data.copy()
    for column, value in filters.items():
        if value is not None:
            filtered_data = filtered_data[filtered_data[column] == value]
    return filtered_data['reference']

# Titre de l'application
st.title('Sélection de Bungalows')

# Chargement des données
data = load_data()

# Création des sélecteurs pour chaque colonne
filters = {}
for column in data.columns[2:]:  # Commence à partir de la troisième colonne pour exclure 'reference' et 'sous_famille'
    selected_value = st.selectbox(f'Sélectionnez une valeur pour {column}', [None] + data[column].unique())
    filters[column] = selected_value

# Bouton pour filtrer les références
if st.button('Filtrer'):
    filtered_references = filter_references(data, filters)
    if filtered_references.empty:
        st.write('Aucune référence ne correspond aux critères sélectionnés.')
    else:
        st.write('Références correspondantes :')
        st.write(filtered_references)
