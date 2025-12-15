import requests

def getOperator(Operator):
    response = requests.get(f"https://api.rhodesapi.com/api/operator{Operator.lower()}")
    if response.status_code != 200:
        print("None")
        return "sorry! either operator doesnt exist or error fetching data"
    
    data = response.json()
    return {
        "infection_status": data["infection_status"],
        "rarity": data["rarity"],
        "class": [c["rarity"] for c in data["class"]]
    }

operator = getOperator("Amiya")
print(operator)

# import requests
 
# def getPoke(poke):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
#     if response.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     data = response.json()
#     return {
#         "name": data["name"],
#         "height": data["height"],
#         "weight": data["weight"],
#         "types": [t["type"]["name"] for t in data["types"]]
#     }

# pokemon = getPoke("sunflora")
# print(pokemon)     
