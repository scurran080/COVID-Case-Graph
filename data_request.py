import requests
import json

#Populates the data in the covid_data.json as well as the covid_data_dict.txt
def populate():
   url = "https://covidtracking.com/api/states"
   response = requests.get(url)
   data = json.loads(response.text)
   with open("covid_data.json","w") as output:
      json.dump(data,output)
   result = []
   for item in data:
      inner = []
      inner.append(item["state"])
      inner.append(item["positive"])
      result.append(inner)
   with open("covid_data_dict.txt","w") as outfile:
      outfile.write(str(result))
   return result