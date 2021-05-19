import csv
import json

data = {}

file = open("example.csv", "r")
dict_reader = csv.DictReader(file)

for rows in dict_reader:

            # Passando a chave
    key = rows['column_22']
    data[key] = rows
	

dict_from_csv = list(dict_reader)[0]
json_from_csv = json.dumps(dict_from_csv)

print(json_from_csv)