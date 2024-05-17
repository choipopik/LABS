import json
import csv
import os

def json_to_csv(json_file):
    with open(json_file, 'r') as file:

        data = json.load(file)
        head_name = list(data.keys())[0]
        csv_file_name = file_name[:-5] + ".csv"

        with open(csv_file_name, 'w', newline='') as csv_file:

            writer = csv.writer(csv_file)
            writer.writerow(data[head_name][0].keys())

            for item in data[head_name]:
                writer.writerow(item.values())


file_name = "Sample-employee-JSON-data.json"
json_to_csv(file_name)
