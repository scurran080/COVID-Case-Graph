
def get_values(json_data, id_key, value_key):
   result = []
   for item in json_data:
      inner = []
      inner.append(item[id_key])
      inner.append(item[value_key])
      result.append(inner)
   with open(value_key + "covid_data_dict.txt", "w") as outfile:
      outfile.write(str(result))
   return result

#Enter the date in the same format as they appear in the data ie. YYYYMMdd
#will throw error otherwise
def date_range(data, start_date, end_date, index_in_data = 0):
   trimmed = []
   for item in data:
      if int(item[index_in_data]) >= start_date and int(item[index_in_data]) <= end_date:
         trimmed.append(item)
   trimmed.reverse()
   return trimmed



