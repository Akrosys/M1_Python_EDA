import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.title("TP | Réalisation d'une data app")

# Récupération des fichiers dans le dossier actuel
st.subheader("Sélectionnez un dataset :")
def file_selector(folder_path='./Data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Dataset étudié :', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
df = pd.read_csv(filename)

if filename == './Data\Pokemon.csv':
    st.header("Statistiques des pokémons")
else:
    st.header("Résultats du football intenational depuis 1872")

##Accès aux données du dataset en indiquant le nombre de ligne
st.subheader("Indiquez le nombre de ligne du dataset que vous souhaitez voir :")
number = st.number_input("Nombre de lignes :")
st.dataframe(df.head(int(number)))

##Affichage des noms des colonnes
st.subheader("Les colonnes du dataset :")
st.write(df.columns.tolist())

#Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
st.subheader("Afficher le dataset comme vous le souhaitez")
colonnes = st.multiselect("Selectionnez une colonne :",df.columns.tolist())
st.write("Types :", df[colonnes].dtypes)
st.write("Contenu des colonnes :",df[colonnes])
st.write("Vous avez sélectionné",len(colonnes),"colonnes")

#La shape du dataset, par lignes et par colonnes
st.subheader("Shape du dataset :")
st.write(df.shape)

#Statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(df.describe())

#Heatmap des corrélations
st.subheader("Affichage de la heatMap de correlation")
st.write(sns.heatmap(df.corr(),annot=True))
st.pyplot()

#Graphique en barre
st.subheader("Affichage du graphique en barre")
graphique = st.selectbox("Selectionnez une caractéristiques :",df.columns.tolist())
st.write(sns.barplot(x=df[graphique].value_counts().index[:20], y=df[graphique].value_counts().values[:20]))

if df[graphique].dtype == object:
    plt.xticks(rotation=90)

st.pyplot()

#Visualisation personnalisable
st.subheader("Fabriquez votre propre graphique")
carac1 = st.selectbox("Choisir une caractéristique en abscisse :", df.columns.tolist())
carac2 = st.selectbox("Choisir une caractéristique en ordonnée :", df.columns.tolist())

if carac1 == carac2:
    st.error("Impossible d'obtenir un graphique avec les memes caractèristiques")
else:
    sns.boxplot(data=df)
    st.pyplot()
    
if st.button("Thanks"):
        st.balloons()
