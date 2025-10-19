import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données['ca'] = données['prix'] * données['qte']
figure = px.pie(données, values='ca', names='produit', title='chiffre affaires par produit')

figure.write_html('chiffre_affaires_par_produit.html')

print('chiffre_affaires_par_produit.html généré avec succès !')