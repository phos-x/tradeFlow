import requests
import csv
import os
from datetime import datetime
from api_config import api_functions, ACCESS_KEY


def fetch_api_data(base_url, api_function, **kwargs):
    if api_function not in api_functions:
        raise ValueError(f"Unsupported API function: {api_function}")
    
    required_params = api_functions[api_function]["required_params"]
    for param in required_params:
        if param not in kwargs:
            raise ValueError(f"Missing required parameter: {param}")
    
    endpoint_path = api_functions[api_function]["endpoint"]
    endpoint = f"{base_url}/{endpoint_path}"

    default_params = api_functions[api_function].get("default_params", {})
    if default_params:
        kwargs.update(default_params)
    params = {"access_key": ACCESS_KEY, "default_params":default_params, **kwargs}

    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()

def save_to_csv(data, output_file):
    if "data" not in data or not isinstance(data["data"], list):
        raise ValueError("Invalid or missing data in response.")
    
    records = data["data"]
    
    file_exists = os.path.isfile(output_file)
    with open(output_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            headers = records[0].keys()
            writer.writerow(headers)
        
        for record in records:
            writer.writerow(record.values())
