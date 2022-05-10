

    
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:33:44 2022

@author: PHAM NGOC SA Clément
"""

import streamlit as st
#from streamlit_option_menu import option_menu
#import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
#import opencv2
import pandas as pd
#import matplotlib.pyplot as plt

#import seaborn as sns
# from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
import plotly.express as px

#from plotly.subplots import make_subplots
#import plotly.graph_objects as go

import io 

st.set_page_config(page_title= 'Marketing Campaign - Prédiction la souscription au produit à term', 
                    layout="wide",
                    initial_sidebar_state="expanded")

st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    
    
    choose = option_menu("Projet Py-MBANK",  ["I. Introduction", 
                                              "II. Approche",
                                              "III. Exploration du jeu de données", 
                                              "IV. Visualisation de données", 
                                              "V. Modélisation",
                                              "VI. Conclusion",
                                              "VII. Recommendations"
                                              ],
                         
                         
                         icons=['currency-exchange', 
                                'currency-exchange', 
                                'currency-exchange', 
                                'currency-exchange',
                                'currency-exchange', 
                                'currency-exchange',
                                'currency-exchange'],
                         menu_icon="bank", default_index=0,
                         
                         
                         styles={
                                 "container": {"padding": "5!important", "background-color": "#E0ECF8"},
                                 "icon": {"color": "black", "font-size": "15px"}, 
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                 "nav-link-selected": {"background-color": "#FE9A2E"},
    }
    )
    
    # séparer le menu1
    st.text("----------***********----------")
    
    
   
   
    # Nom des auteurs et superviseur
    with st.container():
        st.header("Promotion Data Analyst (Formation Continue):")
        st.subheader("Octobre 2021 - Mai 2022")
        st.subheader("Auteurs :")
        st.text("Liliane NYINAWINEZA")
        st.text("Aichetou KETOUOP")
        st.text("Clément PHAM NGOC SA")
        st.text("Steve NGOMEZO ")
    
        st.subheader("Superviseur:")
        st.text("Emilie GREFF ")
        
        style = { "container": {"padding": "5!important", "background-color": "#E0ECF8"},
                 "nav-link-selected": {"background-color": "#FE9A2E"},} 
    
# ----------------Commencer le contenu 
    
# Page I : Introduction


if choose == "I. Introduction":
    
    # Title of page
    st.header("Prédiction des soucriptions au 'dépôt à terme'")
    
    
    #Insert image
    col1, col2, col3 = st.columns([2,6,1])
    with col1: 
        st.write("")
    with col2: 
        image1 = Image.open(r'C:/Users/PHAM Clément/Documents/PROJET_DATASCIENTEST/bank_cda/Image2_projet_MBANK.jpg') 
        st.image(image1, width = 280)
    with col3:
        st.write("")
    
    
    # Begin the content : 
    
    st.header("Introduction du projet")
    
    st.subheader("1. Contexte ")  
    contexte = (" Dans le cadre de lancement d’un nouveau produit : <dépôt à terme> une banque européenne met en place une campagne de \
                  télémarketing. Cette campagne vise à obtenir la souscription à ce dépôt : Le client place une somme d’argent sur un compte\
                bloqué, et percevra des intérêts de la part de la banque après un certain temps. Pour cela, la banque va contacter des milliers \
                de clients pour leur proposer de souscrire à ce produit. Les clients contactés ont des profils différents selon leur données \
                personnelles telles que : L’âge, le statut marital, le solde qu’ils ont sur leur compte, le crédit immobilier, le nombre de fois \
                qu’ils ont été contactés… " )
    
    st.write(contexte)
        
    st.subheader("2. Objectifs ")  
    objectifs = (" Sur la base d’un jeu de données 'bank.csv', nous effectuons une analyse visuelle et statistique des facteurs pouvant expliquer ou identifier les liens entre les données personnelles du client et la variable ' cible ' Le déposit. Utiliser les techniques de Machine Learning afin de construire les modèles de prédiction si les clients adhèrent à cette offre. Définir le profil des clients qui sont susceptibles d’accepter cette offre.")
    st.write(objectifs)
    
#--------Aproches / plan du projet    
    
if choose == "II. Approche":
    st.header(" Approche")
    st.markdown("Ce projet traite un problème de Machine learning , cas de *classification*.\
            Ainsi nous avons entrainé des modèles différents pour comparer les scores\
             et prédire les clients qui vont souscrire à l'offre 'dépôt à terme'")
    if st.checkbox('Preprocessing'):
        st.subheader ("L'exploration des données")
        st.markdown("La première étape est l'exploration des données : elle consiste à:")
        st.text('Comprendre la description des données')
        st.text('Supprimer les valeurs aberrantes')
        st.text('Supprimer les valeurs dupliquées')
        st.text('Encodage des variables')
    if st.checkbox ('La visualisation'):
        st.subheader('Représentation graphique des données')
        st.markdown('Cette étape permet de montrer les liens qui existent entre les variables')
    if st.checkbox("La variable à expliquer et les variables explicatives"):
        st.subheader('La variable cible et les variables explicatives')
        st.markdown("La troisième  étape est de diviser le dataset en 2 parties: variables explicatives(data) d'une part et la variable cible(target) d'une autre part")
        st.text("data : l'ensemble des variables explicatives")
        st.text('target : la variable cible')
    if st.checkbox("Jeu d'entrainement et jeu de test"):
        st.subheader("jeu d'entrainement : 80% et jeu de test 20%")
        st.markdown("Cette étape a pour objectif de mettre de côté un jeu de données : test\
                 qui va être utilisé pour tester le modèle")
        st.text("X_train : jeu d'entrainement")
        st.text("X_test : jeu de test")
    if st.checkbox('La Normalisation'):
        st.subheader('Centrer réduire les variables')
        st.markdown("La normalisation sert à mettre toutes les données sur la même échelle et \
             à améliorer les résultats")
    if st.checkbox("Les modèles de classification"):
        st.subheader('Les modèles de classifications choisis sont:')
        st.text('Regression Logistique')
        st.text('Random Forest')
        st.text('Arbre de décision')
        st.text('Suppor Vector Machine')
        st.text('KNeighbors Classifier')
    
        
        
    
## ------Exploration du jeu de donnés
if choose == "III. Exploration du jeu de données":
    st.header("Exploration du jeu de données") 
    

    st.subheader(" 1. Source du jeu de données")
    st.text(" Les données analysées dans ce projet proviennent de la plateforme")
    st.text(" Kaggle: 'https://www.kaggle.com/ruthgn/bank-marketing-data-set' ")


    st.subheader(" 2. Information et aperçu du dataset bank.csv")
    st.write("Le dataset est composé de 17 colonnes et concerne 11 162 clients, n'a pas de valeurs nulles, pas de NA, pas de valeurs dupliquées. ")


    ### II.Afficher le jeu de donnés
    #df = pd.read_csv("bank.csv")
    #st.dataframe(df)

    # mettre du code
    with st.echo():
        
        df = pd.read_csv("bank.csv")
        df.isna().sum()
        df.duplicated()
        df.info()
       

    #checkbox
    ## Afficher le jeu de donnés
    if st.checkbox("Afficher le jeu de données"):
        st.dataframe(df)

    ## Vérifier les valeurs NAs
    if st.checkbox("Afficher les valeurs manquantes") :
        st.dataframe(df.isna().sum())  
        
    ## Vérifier les valeurs dupliquées  
    if st.checkbox("Afficher les valeurs dupliquées") : 
        st.dataframe(df.duplicated())   
        
    if st.checkbox("Afficher les infos sur les variables") : 
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    
    st.subheader(" 3. Description les variables numériques ")
    # Description des variables numériques 
    with st.echo():   # mettre du code
        df.describe()
    if st.checkbox("Afficher la description des variables numériques"):
        st.dataframe(df.describe())
    
    
    st.subheader(" 4. Description les variables catégorielles ")
    with st.echo():
        
        # Variables catégorielles
        df_cat  = df.select_dtypes(include =['object'])
        for col in df_cat.columns:
            print(df_cat[col].value_counts().reset_index())
        
    if st.checkbox("Afficher les variables catégorielles"):
        df_cat  = df.select_dtypes(include =['object']) 
        for col in df_cat.columns:
            df_cat_values = pd.DataFrame(df_cat[col].value_counts().reset_index())
            st.table(df_cat_values )
            
    



# --------------III Visualisation de donnés
if choose == "IV. Visualisation de données":
    st.header("Visualisation de données") 
    df = pd.read_csv("bank.csv")
    
    # Affiche le graph deposit
    st.subheader("1. La variable cible : 'deposit' ")
    
    with st.expander("Afficher la figure de la variable cible : 'deposit'"):
        col1, col2 =st.columns([2,1])
        with col1:
            
            tab_deposit = df.deposit.value_counts()
    
            fig_deposit = px.pie(tab_deposit , values = tab_deposit.values, 
                                 names = ['no_deposit', 'yes_deposit' ],
                                 color_discrete_sequence = ['red', 'blue'],
                                 labels = tab_deposit.index, 
                                 width = 600, height = 400, 
                                 title="le taux 'yes/no' de la variable 'deposit' ")
            st.plotly_chart(fig_deposit, use_container_width=True)
            
  
                
        with col2:
            st.write(" La variable cible est « déposit » : C’est une variable catégorielle qui a 2 modalités : yes ou no.")
            st.write("Yes : Le client s’intéresse au produit « dépôt à terme » et décide de souscrire")
            st.write("No : Le client n’est pas intéressé par l’offre et décide de ne pas souscrire")

    
    
    
        
    # Les variables catégorielles avec variable cible
    st.subheader("2. Les variables catégorielles et variable cible: ")
    
    with st.expander("Afficher la figure : les variables catégorielles et la variable 'deposit' "):
        
        selected_cat = st.selectbox("Chosissez la variable à afficher le figure", 
                                    ['job', 'marital', 'education', 'default', 'housing', 'loan','contact', 'month', 'poutcome'],
                                    key = 'category_deposit')
                                   
        col3, col4 = st.columns([2,1])
        with col3: 
            if selected_cat == 'job':
                   fig2 = px.histogram(df , x= df['job'], color = df['deposit'], width =800, height=400, 
                                       title = "Souscription des clients selon le métier ",
                                       barmode = 'group')
                   st.plotly_chart(fig2, use_container_width=True)
        
            elif selected_cat == 'marital':
               fig3 = px.histogram(df , x= df['marital'], color = df['deposit'], width =800, height=400, 
                                       title = "Souscription des clients selon le situation matrimoniale ",
                                       barmode = 'group')
               st.plotly_chart(fig3, use_container_width=True)
        
            elif selected_cat == 'education':
                fig4 = px.histogram(df, x= df['education'], color = df['deposit'], width =800, height=400, 
                                       title = "Souscription des clients selon le niveau d'éducation' ",
                                       barmode = 'group')
                st.plotly_chart(fig4, use_container_width=True)
               
            elif selected_cat == 'housing':
                fig5 = px.histogram(df, x= df['housing'], color = df['deposit'], width =800, height=400, 
                                        title = "Souscription des clients selon le niveau de crédit immobilier ",
                                        barmode = 'group')
                st.plotly_chart(fig5, use_container_width=True)
                
            elif selected_cat == 'loan':
                fig6 = px.histogram(df, x= df['loan'], color = df['deposit'], width =800, height=400, 
                                        title = "Souscription des clients selon le niveau de crédit de consommation' ",
                                        barmode = 'group')
                st.plotly_chart(fig6, use_container_width=True)
            
            elif selected_cat == 'default':
                fig7 = px.histogram(df, x= df['default'], color = df['deposit'], width =800, height=400, 
                                        title = "Souscription des clients selon le niveau de défaut de paiement ",
                                        barmode = 'group')
                st.plotly_chart(fig7, use_container_width=True)
                
            elif selected_cat == 'contact':
                fig8 = px.histogram(df, x= df['contact'], color = df['deposit'], width =800, height=400, 
                                        title = "Souscription des clients selon le contact ",
                                        barmode = 'group')
                st.plotly_chart(fig8, use_container_width=True)
            
            elif selected_cat == 'month':
                fig9 = px.histogram(df, x= df['month'], color = df['deposit'], width =800, height=400, 
                                        title = "Souscription selon le mois de contact ",
                                        barmode = 'group')
                st.plotly_chart(fig9, use_container_width=True) 
                
            elif selected_cat == 'poutcome':
                fig10 = px.histogram(df, x= df['poutcome'], color = df['deposit'], width =800, height=400, 
                                 title = "Souscription des clients selon le résultat de la précédente campagne ",
                                 barmode = 'group')
                st.plotly_chart(fig10, use_container_width=True)            
           
        with col4:
            if selected_cat == 'job':
                st.write(" Les « management », « blue-collar » et « technician » sont les plus contactés. Cependant, ils ne sont \
                             pas assez nombreux à souscrire. Les « services », « les entrepreneurs » et les « self-employed » n’ont pas \
                             une forte proportion parmi les clients contactés, et n’ont pas répondu positivement à la proposition. \
                            Cependant l’offre est plus attractive chez les « students », les « unemployed » et les « retired », \
                            malgré leur faible représentativité parmi les clients abordés par la banque.")
            
            if selected_cat == 'marital':
                st.write("Il ressort que les célibataires sont intéressés au produit contrairement aux mariés où on observe un préférence \
                         nette à ne pas souscrire au produit. Et du côté des divorcés il n y a pas de préférence particulière au produit\
                             qui se dégage")

                
            elif selected_cat == 'education':
                st.write(" On remarque que les personnes qui ont le niveau d'étude le plus élevé(tertiary) sont les plus intéressées au produit.")
    
            if selected_cat == 'housing':
                st.write("Presque 50% des clients ont déjà contractés un crédit   immobilier ")
                st.write(" Les clients n'ayant pas de crédit immobilier sont plus sensibles au produit 'dépôt à terme' ")
               
               
            if selected_cat == 'loan':
                st.write("•	La plupart des clients n’ont pas des prêts à la consommation :")
                st.write(      "1460 ont un crédit à la consommation contre")
                st.write(      " 9702 qui n’ont pas de crédit")
               
               
            
            if selected_cat =='default' :
                st.write(" IL y a très peu de clients qui ont un défaut de paiement")

            if selected_cat =='contact' :
                st.write(" Ceux dont on dispose d'un moyen de contact bien identifié ont souscrit au produit à terme ")
             
            if selected_cat =='month' :
                st.write(" Le mois de Mai est celui où les clients ont été le plus contacté ")
                
            if selected_cat =='poutcome' :
                st.write(" Cette variable representante le résultat de la dernière campagne de souscription et il ressort un nombre \
                         important 75% qui ne represente ni une réussite ni un échec ")  
      
    # Les variables numériques avec variable cible
    st.subheader("3. Les variables numériques avec la variable cible: ")      
    with st.expander("Afficher la figure : Les variables numériques avec la variable cible ") : 
        # Commentaire 
        st.write(" • Les variables 'balance', 'duration', 'campaign', 'pdays' et 'previous' sont fortement biaisés vers la gauche et semble \
                 avoir des valeurs aberrantes. ")
        st.write(" • La variable “âge”  a quelques outliers dont les valeurs sont supérieures à 90 ans parmi les souscripteurs")
        st.write(" • La variable balance montre des valeurs aberrantes au-delà de 40 000.")
        selected_cat = st.selectbox("Chosissez la variable à afficher le figure", 
                                    ['age', 'balance', 'previous', 'pdays', 'day', 'duration'],
                                    key = 'numeric_deposit')
        
        if selected_cat == 'age':
               fig_num1 = px.histogram(df, x= "age", color = 'deposit', 
                                                    width = 800, height=400,  marginal="box",  
                                                    hover_data=df.columns, 
                                                    title = "Souscription des clients enfonction de 'age' ",
                                                    barmode = 'group')
             
               st.plotly_chart(fig_num1, use_container_width=True)
    
        if selected_cat == 'balance':
            fig_num2 = px.histogram(df, x= "balance", color = 'deposit', 
                                                 width = 800, height=400,  marginal="box",  
                                                 hover_data=df.columns, 
                                                 title = "Souscription des clients en fonction de 'balance' ",
                                                 barmode = 'group')
          
            st.plotly_chart(fig_num2, use_container_width=True)
        
        if selected_cat == 'previous':
            fig_num3 = px.histogram(df, x= "previous", color = 'deposit', 
                                                 width = 800, height=400,  marginal="box",  
                                                 hover_data=df.columns, 
                                                 title = "Souscription des clients en fonction de 'previous' ",
                                                 barmode = 'group')
          
            st.plotly_chart(fig_num3, use_container_width=True)
    
        if selected_cat == 'pdays':
            fig_num4 = px.histogram(df, x= "pdays", color = 'deposit', 
                                                 width = 800, height=400,  marginal="box",  
                                                 hover_data=df.columns, 
                                                 title = "Souscription des clients en fonction de 'pdays' ",
                                                 barmode = 'group')
          
            st.plotly_chart(fig_num4, use_container_width=True)
            
        if selected_cat == 'day':
            fig_num5 = px.histogram(df, x= "day", color = 'deposit', 
                                                 width = 800, height=400,  marginal="box",  
                                                 hover_data=df.columns, 
                                                 title = "Souscription des clients en fonction de 'day' ",
                                                 barmode = 'group')
          
            st.plotly_chart(fig_num5, use_container_width=True)
            
        if selected_cat == 'duration':
            fig_num6 = px.histogram(df, x= "duration", color = 'deposit', 
                                                 width = 800, height=400,  marginal="box",  
                                                 hover_data=df.columns, 
                                                 title = "Souscription des clients en fonction de 'duration' ",
                                                 barmode = 'group')
          
            st.plotly_chart(fig_num6, use_container_width=True)
    
    
    
    # Corrélation entre les variables numériques
    st.subheader("4. La corrélation entre les variables numériques : ") 
    with st.expander("Afficher la figure : Relation des variables quantitatives "):  
        fig = plt.figure(figsize=(10, 4)) 
        sns.heatmap(df.corr(), annot = True, cmap = 'viridis', vmax = 0.5)
        st.pyplot(fig)
       
        st.write(" On observe que les variables numériques sont très peu corrélées entre elles sauf les 2 variables 'pdays' et 'previous' qui sont des mesures pour les précédentes campagnes.")
    
              
    # Les Croissements des variables explicatives         
    st.subheader("5. Les croissements des variables explicatives : ")
    with st.expander("Afficher la figure : Les croissements des variables explicatives"):  
        chart_visual = st.selectbox("Choisir le 'Charts/Plot' type", ('Line Chart', 'Bar Chart'))
        st.markdown(" Bar Chart : 'job' et 'housing' / 'job' et 'loan'/ 'contact' et 'poutcome' ")
        st.markdown(" Line Chart: 'job' et 'age'/ 'job' et 'housing' / 'job' et 'loan'")
        
        selected_variable1 = st.selectbox("Choisir variable 1", ['job','age', 'contact'])
        selected_variable2 = st.selectbox("Choisir variable 2", [ 'housing', 'loan', 'age', 'poutcome'])

    # fig = go.Figure()
    
    
        if chart_visual == 'Bar Chart':
            if selected_variable1 == 'age' : 
                if selected_variable2 == 'housing': 
                    tab_age_housing_deposit = df.groupby(["age", "deposit", "housing" ]).size().reset_index(name = 'count') 
                    fig1_1 = px.bar(tab_age_housing_deposit, x= "age" , y="count",  facet_col= "housing", color="deposit", barmode="overlay",   
                              title = "Le croissement  'age' avec  'housing' et 'deposit'",  
                              category_orders={"deposit": ["yes", "no"]})
                    st.plotly_chart(fig1_1, use_container_width=True)
              
                if selected_variable2 == 'loan': 
                    tab_age_loan_deposit = df.groupby(["age", "deposit", "loan" ]).size().reset_index(name = 'count') 
                    fig1_2 = px.bar(tab_age_loan_deposit, x= "age" , y="count",  facet_col= "loan", color="deposit", barmode="overlay",   
                              title = "Le croissement  'age' avec  'loan' et 'deposit'",  
                              category_orders={"deposit": ["yes", "no"]})
                    st.plotly_chart(fig1_2, use_container_width=True)
                
            if selected_variable1 == 'job' : 
                if selected_variable2 == 'housing': 
                    tab_job_housing_deposit = df.groupby(["job", "deposit", "housing" ]).size().reset_index(name = 'count') 
                    fig1_3 = px.bar(tab_job_housing_deposit, x= "job" , y="count",  facet_col= "housing", color="deposit", barmode="overlay",   
                              title = "Le croissement  'job' avec  'housing' et 'deposit'",  
                              category_orders={"deposit": ["yes", "no"]})
                    st.plotly_chart(fig1_3, use_container_width=True)
              
                if selected_variable2== 'loan': 
                    tab_job_loan_deposit = df.groupby(["job", "deposit", "loan" ]).size().reset_index(name = 'count') 
                    fig1_4 = px.bar(tab_job_loan_deposit, x= "job" , y="count",  facet_col= "loan", color="deposit", barmode="overlay",   
                              title = "Le croissement  'job' avec  'loan' et 'deposit'",  
                              category_orders={"deposit": ["yes", "no"]})
                    st.plotly_chart(fig1_4, use_container_width=True)
            
            if selected_variable1 == 'contact' :  
                if selected_variable2 == 'poutcome':
                    tab_contact_poutcome_deposit = df.groupby(["contact", "deposit", "poutcome" ]).size().reset_index(name = 'count') 
                    fig1_4 = px.bar(tab_contact_poutcome_deposit, x= "contact" , y="count",  facet_col= "poutcome", color="deposit", 
                                    barmode="group",   
                                    title = "Le croissement  'contact' avec  'poutcome' et 'deposit'",  
                                    category_orders={"deposit": ["yes", "no"]})
                    st.plotly_chart(fig1_4, use_container_width=True)
                    st.write(" On observe que le moyen de contact le plus utilisé est « cellular » et que les résultats de la campagne précédente ne sont pas connus pour la plupart des clients. ")
                    st.write(" En combinant les variables : moyen de contact et résultat de la campagne précédente, ")
                    st.write("il est clair que les clients qui répondent favorablement à cette offre sont ceux dont la campagne précédente a été un succès et qui sont contactés par téléphone.")
                
        elif chart_visual == 'Line Chart':
            if selected_variable1 == 'age' : 
                if selected_variable2 == 'housing': 
                    tab_age_housing = df.groupby(['age', 'housing']).agg({'balance':'mean'})
                    tab_age_housing.reset_index(level = 0, inplace = True)
                    tab_age_housing.reset_index(level = 0, inplace = True)
                    st.dataframe(tab_age_housing)
                    fig2_1 = px.line(tab_age_housing, x = 'age', y = 'balance', color = 'housing', markers = 'True',
                                     title = "le montant de dépôt moyen en fonction de l'age'regroupé par le crédit immobilier")
                    st.plotly_chart(fig2_1, use_container_width=True)
                    
                if selected_variable2 == 'loan': 
                     tab_age_loan = df.groupby(['age', 'loan']).agg({'balance':'mean'})
                     tab_age_loan.reset_index(level = 0, inplace = True)
                     tab_age_loan.reset_index(level = 0, inplace = True)
                     st.dataframe(tab_age_loan)
                     fig2_2 = px.line(tab_age_loan, x = 'age', y = 'balance', color = 'loan', markers = 'True',
                                      title = "le montant de dépôt moyen en fonction de l'age' regroupé par le crédit consommation")
                     st.plotly_chart(fig2_2, use_container_width=True)
            
            
            if selected_variable1 == 'job' : 
                if selected_variable2 == 'housing': 
                    tab_job_housing = df.groupby(['job', 'housing']).agg({'balance':'mean'})
                    tab_job_housing.reset_index(level = 0, inplace = True)
                    tab_job_housing.reset_index(level = 0, inplace = True)
                    st.dataframe(tab_job_housing)
                    fig2_3 = px.line(tab_job_housing, x = 'job', y = 'balance', color = 'housing', markers = 'True',
                                     title = 'le montant de dépôt moyen en fonction du métier regroupé par le crédit immobilier')
                    st.plotly_chart(fig2_3, use_container_width=True)
                    
                    st.write("  •	Le montant de dépôt moyen varie en fonction des métiers et en fonction du crédit immobilier ")
                    st.write("  •	En effet : Les clients qui ont un crédit immobilier ont le montant moyen plus bas de solde en compte que ceux qui ont juste un crédit à la consommation.")
                    st.write("  •	Les managements, retired et self employed ont plus de dépôt par rapport aux autres clients.")
                                

                    
                if selected_variable2 == 'loan': 
                     tab_job_loan = df.groupby(['job', 'loan']).agg({'balance':'mean'})
                     tab_job_loan.reset_index(level = 0, inplace = True)
                     tab_job_loan.reset_index(level = 0, inplace = True)
                     st.dataframe(tab_job_loan)
                     fig2_4 = px.line(tab_job_loan, x = 'job', y = 'balance', color = 'loan', markers = 'True',
                                      title = 'le montant de dépôt moyen en fonction du métier regroupé par le crédit consommation')
                     st.plotly_chart(fig2_4, use_container_width=True)
                     
                if selected_variable2 == 'age': 
                     tab_job_age = df.groupby(df['job']).agg({'age':'mean'}) 
                     tab_job_age.reset_index(level = 0, inplace = True)
                     st.dataframe(tab_job_age )
                     fig2_5 = px.line(tab_job_age, x = 'job', y = 'age', markers = 'True', title = "L' âge moyen selon les métiers")
                     st.plotly_chart(fig2_5, use_container_width=True)
                     
                     
    # Test statistique entre variable cible avec les variables numérique         
    st.subheader("6. Les tests statistiques : ")
    from scipy.stats import chi2_contingency
    with st.expander("Afficher les Tests statistiques "):  
        if st.checkbox(" Test entre deposit et Housing"):
        
        # La table de contingence
        
            st.write("Ho : Les variables Deposit et Housing sont indépendantes ")
            st.write("H1 : Les variables Deposit et Housing sont dépendantes ")
            
            with st.echo() :
                table_1 = pd.crosstab(df['deposit'],df['housing'])
                table_1
        
                resultats_test = chi2_contingency(table_1)
                statistique = resultats_test[0]
                p_valeur = resultats_test[1]
                degre_liberte = resultats_test[2]

            st.write("statistique =",statistique, "p_valeur =", p_valeur, "degre_liberté =", degre_liberte)
            st.write("On constate que p_valeur <<< 0.05, On rejette l'hypothèse d'indépendance de 2 variables ")
        
        if st.checkbox(" Test entre deposit et contact"):
            with st.echo():
                table_2 = pd.crosstab(df['deposit'],df['contact'])
                table_2
                resultats_test = chi2_contingency(table_2)
                statistique = resultats_test[0]
                p_valeur = resultats_test[1]
                degre_liberte = resultats_test[2]

            st.write('statistique =',statistique, 'p_valeur =', p_valeur, 'degre_liberté =', degre_liberte)
            st.write(" On constate que p_valeur <<< 0.05, il existe une relation entre contact et déposit")
       
        if st.checkbox(" Test entre age et balance"):
            with st.echo(): 
                from scipy.stats import pearsonr

                pd.DataFrame(pearsonr(df['age'], df['balance']), index=['pearson_coeff','p-value'], columns=['resultat_test'])
                         
            st.write(" Résultat : p_valeur est égal à 1.171392e-32. Ce qui montre qu' il ya une relation entre les variable âge et balance.  Cette relation est mésurée par le coefficient de person qui est égal à 1.122999e-01.")           





       
        
   
# ------V Modèlisation-------
    

from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler, LabelEncoder
#from sklearn.impute import SimpleImputer
from sklearn.pipeline import  Pipeline
#from sklearn.pipeline import make_pipeline, Pipeline

from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
#from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier  
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score

if choose == "V. Modélisation": 
    
    st.header("Modèle de prédiction des souscriptions au 'dépôt à terme' ")  
    

    # Transformation de données : 
    
    st.subheader("1. Transformation des données")

    #checkbox
    
    if st.checkbox("Afficher le code "):
        
    # mettre du code
        with st.echo(): 
            df = pd.read_csv("bank.csv")     

            # Catégoriser la variable  age
            age = pd.cut(df.age, bins = [17,30,60,100], labels = ['young', 'adult','retired'])
            df['age'] = age.astype('object')

            # remplace "unknown" de variable 'job' par 'unemployed'
            df['job'] = df['job'].replace(to_replace={'unknown': "unemployed"})

            # remplace "unknown" de variable 'education' par 'others'
            df['education'] = df['education'].replace(to_replace={'unknown': 'others' })

            # remplace "unknown" de variable "contact" par "others" (ici je considère que les 'unknown' comme autres moyennes de communication)
            df['contact'] = df['contact'].replace(to_replace={'cellular': 'phone', 'telephone':'phone', 'unknown': 'others'})

            # Transformer poutcome "unknown" en no_exist
            df['poutcome'] = df['poutcome'].replace(to_replace={'unknown':'no_exist', 'other':'failure'})

            # enlever les valeurs abberantes de la variable "balance"
            df = df.loc[(df.balance > -2000) & (df.balance <= 40000)]
            
            # suprimer les valeurs dupliquées
            df.drop_duplicates(keep = 'first', inplace=True)  
            
            # suprimer la variable 'duration'
            df = df.drop(['duration'], axis = 1)
                
           
            
            def split(df) : # Split the data to ‘train and test’ sets  
                col_binaire = ['deposit','default', 'housing','loan', 'contact']
                df[col_binaire]= df[col_binaire].apply(LabelEncoder().fit_transform)
            
                df = pd.get_dummies(df)
            
                target = df.deposit 
                data = df.drop("deposit", axis = 1)
                x_train, x_test, y_train,y_test = train_test_split(data, target, test_size = 0.2, random_state = 123)
                
                df_num_col = ['balance', 'campaign', 'previous', 'day', 'pdays']
                
                scaler = StandardScaler()

                x_train[df_num_col]= scaler.fit_transform(x_train[df_num_col])
                x_test[df_num_col] = scaler.transform(x_test[df_num_col])
                
                
                return  x_train, x_test, y_train, y_test
        
       
            
        
          
    ## Afficher le jeu de donnés
    
    
    df = pd.read_csv("bank.csv")     

    # Catégoriser la variable  age
    age = pd.cut(df.age, bins = [17,30,60,100], labels = ['young', 'adult','retired'])
    df['age'] = age.astype('object')

    # remplace "unknown" de variable 'job' par 'unemployed'
    df['job'] = df['job'].replace(to_replace={'unknown': "unemployed"})

    # remplace "unknown" de variable 'education' par 'others'
    df['education'] = df['education'].replace(to_replace={'unknown': 'others' })

    # remplace "unknown" de variable "contact" par "others" (ici je considère que les 'unknown' comme autres moyennes de communication)
    df['contact'] = df['contact'].replace(to_replace={'cellular': 'phone', 'telephone':'phone', 'unknown': 'others'})

    # Transformer poutcome "unknown" en no_exist
    df['poutcome'] = df['poutcome'].replace(to_replace={'unknown':'no_exist', 'other':'failure'})

    # enlever les valeurs abberantes de la variable "balance"
    df = df.loc[(df.balance > -2000) & (df.balance <= 40000)]
    
    # suprimer les valeurs dupliquées
    df.drop_duplicates(keep = 'first', inplace=True)  
    
    # sumprimer la variable 'duration' :
    #La variable 'duration' est parfaitement corrélée au variable 'deposit'. 
    # La durée d'appel est connu quand les appels se sont terminés. si il n'y pas d'appel, la duration égale 0.
    #  L'existence de cette variable est comme la référence. 
    # On va suprimer cette variable lors modélisation.
    df = df.drop(['duration'], axis = 1)
        
    #df['deposit'] = df['deposit'].replace(to_replace={'yes':1, 'no':0 }) 
    
    
    st.subheader(" Les données après la transformation")
    if st.checkbox("Afficher les données après la transformation "):
        st.dataframe(df) 
        
    def split_1(df, key =2) : # Split the data to ‘train and test’ sets  
        col_binaire = ['deposit','default', 'housing','loan', 'contact']
        df[col_binaire]= df[col_binaire].apply(LabelEncoder().fit_transform)

        df = pd.get_dummies(df)

        target = df.deposit 
        data = df.drop("deposit", axis = 1)
        x_train, x_test, y_train,y_test = train_test_split(data, target, test_size = 0.2, random_state = 123)
    
        df_num_col = ['balance', 'campaign', 'previous', 'day', 'pdays']
    
        scaler = StandardScaler()

        x_train[df_num_col]= scaler.fit_transform(x_train[df_num_col])
        x_test[df_num_col] = scaler.transform(x_test[df_num_col])
    
        if st.checkbox("Afficher data_preproccessing"):
            st.dataframe(df)
        
            st.write("shape data train et data test")
            x_train.shape, x_test.shape, y_train.shape, y_test.shape
            st.write(" Après la transformation des données, on a obtenu :")
            st.write(" + Data train avec 45 colonnes et 8919 lignes")
            st.write(" + Data test avec 45 colonnes et 2230 lignes")
    
        return  x_train, x_test, y_train, y_test    
    x_train, x_test, y_train, y_test = split_1(df)
    
    def plot_metrics(metrics_list):
        
        if 'Confusion Matrix' in metrics_list: 
            st.subheader("Matrice de  confusion (Matrix Confusion)")
            plot_confusion_matrix(model, x_test, y_test, display_labels= class_names)
            st.pyplot()
        if 'ROC Curve' in metrics_list:
            st.subheader("La courbe de ROC (ROC Curve)")
            plot_roc_curve(model, x_test, y_test)
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader(" La courbe de Présision - Rappel (Precision-Recall Curve)")
            plot_precision_recall_curve(model, x_test, y_test)
            st.pyplot() 
    class_names = ['no_deposit', 'yes_deposit']   
    
    
    
    
    
    st.subheader("3. Les modèles avec les paramètres par défaut")
    if st.checkbox(" Afficher le code"):
        with st.echo() :
            # Afficher le code : 
            lr = LogisticRegression()
            knn = KNeighborsClassifier()
            svc = SVC()
            dtc = DecisionTreeClassifier()
            rfc = RandomForestClassifier()

            lr.fit(x_train, y_train)
            knn.fit(x_train, y_train)
            svc.fit(x_train, y_train)
            dtc.fit(x_train, y_train)
            rfc.fit(x_train, y_train)
        
    if st.checkbox(" Afficher les scores avec les paramètres par défaut") :
        st.subheader("Les scores avec data train")
        st.write("modèle logistic regression score avec data train: 0.71")
        st.write("modèle KNN score avec data train: 0.78")
        st.write("modèle SVM score avec data train: 0.75")
        st.write("modèle Decision Tree score avec data train: 0.99")
        st.write("modèle Random Forest score avec data train: 0.99")
    
        st.subheader("Les scores avec data test")
        st.write("modèle logistic regression score avec data test: 0.71")
        st.write("modèle KNN score avec data test: 0.68")
        st.write("modèle SVM score avec data test: 0.74")
        st.write("modèle Decision Tree score avec data test: 0.63")
        st.write("modèle Random Forest score avec data test: 0.71")
    
    
  
    st.subheader("4. Les modèles avec les différentes paramètres")
    with st.expander("Afficher les modèles"):
        st.subheader(" Choisissez - vous un  modèle")
        classifier = st.selectbox("Classifier", ("Logistic Regression", 
                                             "Random Forest", 
                                             "Decision Tree", 
                                             "K Nearest Neighbor (KNN)", 
                                             "Support Vector Machine (SVM)"))
        
        
        
    
    
    # Model Logistic Regression
        if classifier == "Logistic Regression":
            st.subheader("Modèle Paramètres")
            C = st.number_input("C (La régularisation de paramètre)", 0.01, 50.0, step=0.01, key="C_LR")
            max_iter = st.slider("Le nombre d'iterations", 1, 1000, key="max_iter")
            metrics = st.multiselect("Les 'metrics' d'évaluation de modèle", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))  
        
            if st.button("Résultat", key="classify"): 
                st.subheader(" Résultat de 'Modèle Logistic Regression' Résultat : ")
                model = LogisticRegression(C=C, penalty="l2", max_iter=max_iter)
                model.fit(x_train, y_train)
                model.fit(x_train, y_train)
                accuracy_train = model.score(x_train, y_train)
                accuracy_test = model.score(x_test, y_test)
                y_pred = model.predict(x_test)
                st.write("Le score de data_train: ",  accuracy_train.round(2)*100,"%")
                st.write("Le score de data_test: ",  accuracy_test.round(2)*100,"%")
                st.write("Précision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                st.write("Rappel: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                plot_metrics(metrics)
         
    
            
        # Model Random Forest
        if classifier == "Random Forest":
            st.subheader("Modèle Hyperparamètres")
            n_estimators = st.number_input("Le nombre maximum d'arbres", 50, 5000, step=10, key="n_estimators")
            max_depth = st.number_input("Le maximum de l'arbre", 1, 20, step=1, key="n_estimators")
            bootstrap = st.radio("Bootstrap samples when building trees", ("True", "False"), key="bootstrap")
            metrics = st.multiselect("Les 'metrics' d'évaluation de modèle", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve")) 
        
            if st.button("Résultat", key="classify") : 
                st.subheader(" Résultat de 'Modèle Random Forest' : ")
                model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
                model.fit(x_train, y_train)
                model.fit(x_train, y_train)
                accuracy_train = model.score(x_train, y_train)
                accuracy_test = model.score(x_test, y_test)
                y_pred = model.predict(x_test)
                y_pred = model.predict(x_test)
                st.write("Le score de data_train: ",  accuracy_train.round(2)*100,"%")
                st.write("Le score de data_test: ",  accuracy_test.round(2)*100,"%")
                st.write("Précision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                st.write("Rappel: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                plot_metrics(metrics)
        
    
    
        # Model Decision Tree
        if classifier == "Decision Tree": 
            st.subheader("Modèle Paramètres")
            #choose parameters
            criterion= st.radio("Criterion(measures the quality of split)", ("gini", "entropy"), key="criterion")
            splitter = st.radio("Splitter (Comment diviser à chaque  'node' ?)", ("best", "random"), key="splitter")
            metrics = st.multiselect("Les 'metrics' d'évaluation de modèle : ", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve")) 
        
            if st.button("Classify", key="classify"):
                st.subheader(" Le résultat de 'Modèle Decision Tree' ")
                model = DecisionTreeClassifier(criterion=criterion, splitter=splitter)
                model.fit(x_train, y_train)
                model.fit(x_train, y_train)
                accuracy_train = model.score(x_train, y_train)
                accuracy_test = model.score(x_test, y_test)
                y_pred = model.predict(x_test)
                y_pred = model.predict(x_test)
                st.write("Le score de data_train: ",  accuracy_train.round(2)*100,"%")
                st.write("Le score de data_test: ",  accuracy_test.round(2)*100,"%")
                st.write("Précision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                st.write("Rappel: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                plot_metrics(metrics)

        # Model Support Vector Machine (SVM)
        if classifier == "Support Vector Machine (SVM)":
            st.subheader("Modèle Paramètres")
            C = st.number_input("C (La régularisation paramètre)", 0.01, 50.0, step=0.01, key="C_SVM")
            kernel = st.selectbox("Le 'kernel' type", ( 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'), key="kernel_SVM")
            gamma = st.selectbox("Le gamma", ('scale', 'auto'), key="gamma_SVM")
            max_iter = st.slider("Le nombre maximum  d'iterations", -1, 500, key="max_iter")
            metrics = st.multiselect("Les 'metrics' d'évaluation de modèle", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))  
         
            if st.button("Résultat", key="classify"): 
                st.subheader("Le résultat de modèle 'Support Vector Machine (SVM)' :")
                model = SVC(C=C, kernel=kernel, max_iter=max_iter )
                model.fit(x_train, y_train)
                accuracy_train = model.score(x_train, y_train)
                accuracy_test = model.score(x_test, y_test)
                y_pred = model.predict(x_test)
                y_pred = model.predict(x_test)
                st.write("Le score de data_train: ",  accuracy_train.round(2)*100,"%")
                st.write("Le score de data_test: ",  accuracy_test.round(2)*100,"%")
                st.write("Précision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                st.write("Rappel: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                plot_metrics(metrics)
     
        # Model K Nearest Neighbor (KNN)
        if classifier == "K Nearest Neighbor (KNN)":
            st.subheader("Modèle Paramètres")
            n_neighbors = st.number_input("Le nombre de 'neighbors' ", 1 , 11 , key="n_neighbor_KNN")
            algorithm = st.selectbox("L' Algorithm", ( 'auto', 'ball_tree', 'kd_tree'), key="algo_KNN")
            metric = st.selectbox("Choisir le 'metric KNN' ", ('minkowski', 'chebyshev', 'manhattan'), key="metric_KNN")
            metrics = st.multiselect("Les 'metrics' d'évaluation de modèle", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))  
         
            if st.button("Résultat", key="classify"): 
                st.subheader("Le résultat de modèle 'K Nearest Neighbor (KNN)' :")
                model =  KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=algorithm, metric=metric)
                model.fit(x_train, y_train)
                accuracy_train = model.score(x_train, y_train)
                accuracy_test = model.score(x_test, y_test)
                y_pred = model.predict(x_test)
                y_pred = model.predict(x_test)
                st.write("Le score de data_train: ",  accuracy_train.round(2)*100,"%")
                st.write("Le score de data_test: ",  accuracy_test.round(2)*100,"%")
                st.write("Précision: ", precision_score(y_test, y_pred, labels=class_names).round(2))
                st.write("Rappel: ", recall_score(y_test, y_pred, labels=class_names).round(2))
                plot_metrics(metrics)
    
   
    st.subheader("5. Les résultats des modèles avec GridSearch : ")
    if st.checkbox(" Afficher les score des modèles avec GridSearch") :
        
        st.subheader("Les scores avec data train")
        st.write("modèle logistic regression score avec data train: 0.711672278338945")
        st.write("modèle KNN score avec data train: 0.7566778900112233")
        st.write("modèle SVC score avec data train: 0.7565656565656566")
        st.write("modèle Decision Tree score avec data train: 0.7193041526374859")
        st.write("modèle Random Forest score avec data train: 0.7653198653198653")
        
        st.subheader("Les scores avec data test")
        st.write("modèle logistic regression score avec data test: 0.7055655296229802 temps d'éxécution : 5.78 s")
        st.write("modèle KNN score avec data test: 0.7087073608617595 temps d'éxécution : 2min 12s")
        st.write("modèle SVC score avec data test: 0.7387791741472173 temps d'éxécution : 18min 45s")
        st.write("modèle Decision Tree score avec data test: 0.683572710951526 temps d'éxécution : 20.1 s")
        st.write("modèle Random Forest score avec data test: 0.729802513464991 temps d'éxécution : 4min 13s")   
        
        
    
    
##-----VI Conclusion-------------
if choose == "VI. Conclusion" : 
    st.header(" Conclusion:")
    st.write(" Au terme de notre études et aux vu des différents résultats, nous pouvons dire tel que mentionné plus haut que le modèle SVM semble plus fiable en ce qui concerne les prédictions. En effet, parmi les 5 modèles traités avec les paramètres par défaut, c’est le modèle qui nous donne le meilleur score.  ")
    
    st.write(" Il est aussi le modèle le plus stable car le score sur échantillons de test (74%) n'est pas très différent avec le score sur d'échantillons d'apprentissage (75,6%) ce qui nous confirme qu’on n’est pas dans un cas de sous ou de surentraînement. Lorsqu’on applique ce modèle avec les paramètres par défaut on obtient un résultat beaucoup plus rapide que lorsqu’on le combine avec la méthode GridSearch. (En sachant que le temps réalisé avec les paramètres par défaut ne nous prend que 14 second).")
    st.write(" Avec le GridSearch, nous observons que le score sur l'échantillon d'apprentissage de modèle Random Forest est bien amélioré 76,1%, mais il est un peu surapprentissage car le score sur l'échantillon de test est inférieur que le score sur l'échantillon d'apprentissage (72,8%) ")

 ##-----VI Recommendation-------------   
if choose == "VII. Recommendations" :  
    st.header(" Reconmendations:")
    st.write("Pour augmenter le nombre de clients qui souscrivent à ce produit, la banque pourra cibler les profils les plus sensibles à cette offre.")
    st.write(" •	Les étudiants et les retraités ;  ")
    st.write(" •	Les clients qui n’ont pas de crédits de consommation ; ou des crédits immobiliers ; ")
    st.write(" •	Les clients qui possèdent les fonds disponibles à la banque ;  ")
    st.write(" •	Les clients qui ont répondu positivement aux campagnes   ")
    
    st.write(" Le moyen de contact joue aussi un rôle important, le contact par Téléphone serait à privilégier.")
    st.write("Ajuster l’offre aux clients de 30 – 60 ans, car c’est la tranche d’âge la plus représentative dans l’échantillon de donner. ")
    
    st.write(" Plus précisément, cibler un peu plus des clients qui tendent vers 50 à 60 ans car non seulement ils sont proche de la retraite ce qui pourrai les inciter à épargner ou investir, mais en plus le crédit immobilier potentiel est en cours d’être totalement remboursé ce qui leur donnera encore plus de possibilité de souscrire au produit.")
 
 
    
#if __name__ == ‘__main__’:
    #main()
    
    
                    
                           
        

    
  
    
    
   


     
  
