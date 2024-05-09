import json
import csv
import os


def convert_json_to_csv(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

        root_name = list(data.keys())[0]
        csv_file_name = f"{root_name}.csv"

        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Write header
            writer.writerow(data[root_name][0].keys())

            # Write data rows
            for item in data[root_name]:
                writer.writerow(item.values())

    print(f"Successfully converted {json_file} to {csv_file_name}")


json_file = "Sample-employee-JSON-data.json"
convert_json_to_csv(json_file)