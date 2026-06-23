import json

filename=input("Enter filename:")

try:
    with open(filename,"r") as file:
        data=json.load(file)

    print("\n----- JSON Data -----")
    print(json.dumps(data, indent=4))    

except FileNotFoundError:
    print("Error: File not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format.")    
