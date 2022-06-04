import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "lrJISwXVAEURybugnwUNrBxSLuUtTWUy"


class FlightSearch:

    def destination_code(self, city_name):
       headers = {
           "apiKey": TEQUILA_API_KEY
       }
       param={
           "term":city_name,
           "location_type":"city"
       }
       response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",params=param,headers=headers)
       print(response.json())
       results = response.json()["locations"]
       code = results[0]["code"]
       return code