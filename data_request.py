import requests
import json

STATES_DATA = "https://covidtracking.com/api/states"
DAILY_DATA = "https://api.covidtracking.com/v1/us/daily.json"


#Populates the data in the text file and the json file
def request_data(url):
   url = url
   response = requests.get(url)
   data = json.loads(response.text)
   with open("covid_data.json","w") as output:
      json.dump(data,output)
   return data