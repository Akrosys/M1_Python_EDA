import streamlit as st
import pandas as pd
import seaborn as sns

st.title("TP | Réalisation d'une data app")

#Dataset : Football international
st.header("Résultats du football international depuis 1872")
#Import du dataset
dataFootball = pd.read_csv("results.csv")

##Accès aux données du dataset en indiquant le nombre de ligne
st.subheader("Indiquez le nombre de ligne du dataset que vous souhaitez voir :")
number = st.number_input("Nombre de lignes :")
st.dataframe(dataFootball.head(int(number)))

##Affichage des noms des colonnes
st.subheader("Les colonnes du dataset :")
st.write(dataFootball.columns.tolist())

#Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
st.subheader("Afficher le dataset comme vous le souhaitez")
colonnes = st.multiselect("Selectionnez une colonne :",dataFootball.columns.tolist())
st.write("Types :", dataFootball[colonnes].dtypes)
st.write("Contenu des colonnes :",dataFootball[colonnes])
st.write("Vous avez sélectionné",len(colonnes),"colonnes")

#La shape du dataset, par lignes et par colonnes

#Heatmap des corrélations
if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
    st.write(sns.heatmap(dataFootball.corr(),annot=True))
    st.pyplot()