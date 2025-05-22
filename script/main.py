import os
from api_config import api_functions, ACCESS_KEY
from script_engine import fetch_api_data, save_to_csv

# Constants
api_base_url = "http://api.marketstack.com/v2"
output_file = "trading_data.csv"

ACCESS_KEY = os.getenv("ACCESS_KEY", "your_default_access_key_here")

def main():
    print("Available API functions:")
    for idx, func in enumerate(api_functions, start=1):
        print(f" {idx}. {func}")
    
    user_input = input("Enter API function or its index number: ").strip()
    if user_input.isdigit():
        index = int(user_input)
        if 1 <= index <= len(api_functions):
            api_function = list(api_functions.keys())[index - 1]
        else:
            raise ValueError("Invalid index number.")
    else:
        if user_input in api_functions:
            api_function = user_input
        else:
            raise ValueError("Invalid API function name.")
    
    # Collect required parameters
    params = {}
    for param in api_functions[api_function]["required_params"]:
        params[param] = input(f"Enter value for {param}: ").strip()
    
    try:
        data = fetch_api_data(api_base_url, api_function, **params)

        save_to_csv(data, output_file)
        print(f"Data for {api_functions[api_function]} saved to {output_file}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()