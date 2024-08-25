import json
import csv
import os

def json_to_csv(json_file_name, csv_file_name):
    # Define the assets directory
    assets_dir = 'assets'
    
    # Construct the full paths for the input and output files
    json_file_path = os.path.join(assets_dir, json_file_name)
    csv_file_path = os.path.join(assets_dir, csv_file_name)
    
    # Read JSON data from file
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")
        return
    
    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        # If JSON data is a list of dictionaries, use the first dictionary to get column names
        if isinstance(data, list):
            if len(data) == 0:
                # Handle empty list
                print("The JSON file is empty.")
                return
            
            # Get the keys of the first dictionary as the CSV column headers
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            # Write the data rows
            csv_writer.writerows(data)
        elif isinstance(data, dict):
            # In case JSON is a single dictionary, treat keys as columns and the values as a single row
            csv_writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            csv_writer.writeheader()
            csv_writer.writerow(data)
        else:
            print("Unsupported JSON format. Please provide a JSON object or an array of JSON objects.")
            return

    print(f"Data from {json_file_path} has been successfully written to {csv_file_path}.")
