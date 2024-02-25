import requests
import re

url = "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"

querystring = {"fromEntityId":"eyJlIjoiOTU2NzQwNTUiLCJzIjoiR1ZBIiwiaCI6IjMzNzM1OTg1IiwidCI6IkFJUlBPUlQifQ===","toEntityId":"eyJlIjoiMTA0MTIwMjI4IiwicyI6IlROUiIsImgiOiIyNzU0NzIyNSIsInQiOiJBSVJQT1JUIn0=","departDate":"2024-08-15","returnDate":"2024-09-06","currency":"CHF"}

headers = {
	"X-RapidAPI-Key": "c3cfbad934msh669bb01d0b341a2p149484jsnc35baaf3b368",
	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}




def find_formatted_prices() -> int :

    response = requests.get(url, headers=headers, params=querystring)

    reponse =str(response.json())

    # Expression régulière pour rechercher le format 'CHF X,XXX' où X représente des chiffres
    pattern = r"CHF [\d,]+"

    # Recherche de toutes les occurrences dans le texte
    matches = map(lambda x :int((x.replace(",","").replace("CHF ",""))),re.findall(pattern, reponse))

    cheapper = min(matches)
    return cheapper
    

def getLastPrice():
    return find_formatted_prices()


print(getLastPrice())