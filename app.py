import requests

def getOperator(Operator):
    response = requests.get(f"https://api.rhodesapi.com/api/operator/{Operator.lower()}")
    if response.status_code != 200:
        print("error getting data srry")
        return "trouble fetching data"
    
    data = response.json()
    return {
        "name": data["name"],
        "infection_status": data["infection_status"],
        "rarity": data["rarity"],
        "biography": data["biography"],
        "class": [c["name"] for c in data["class"]]
    }

operator = getOperator("ines")
print(operator)

