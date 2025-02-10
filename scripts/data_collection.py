import requests
import pandas
import json

#clé Api recupéreé depuis alphavantage

API_KEY="R4PNUDGJMOHBWPRO"

#liste des entreprises
entreprise=["AAPL","MSFT","GOOGL","AMZN"]



#base de l'url
BASE_URL = "https://www.alphavantage.co/query"

#structure pour stocker les données de chaque entreprise

entreprises_data={}


#recuperer les données pour chaque entreprise

for i in entreprise:

    #parametre pour l'api 
    params_fundamentals={
        "function":"OVERVIEW",
        "symbol":i,
        "apikey":API_KEY
        
        

    }


    fundamentals_response = requests.get(BASE_URL, params=params_fundamentals)
    if fundamentals_response.status_code == 200:
        fundamentals_data = fundamentals_response.json()
        entreprises_data[i]=fundamentals_data
        
    else:
        print(f"Erreur lors de la récupération des données fondamentales pour {i}")

with open("fundamental.json", "w") as f:
    json.dump(entreprises_data, f, indent=4)

