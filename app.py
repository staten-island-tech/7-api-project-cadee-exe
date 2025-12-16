import requests

def getOperator(Operator):
    response = requests.get(f"https://api.rhodesapi.com/api/operator{Operator.lower()}")
    data = response.json()
    if response.status_code != 200:
        print("Nothing")
        return "sorry! either operator doesnt exist or error fetching data"
    else:
        return {
        data
    }
operator = getOperator("Flametail")


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

