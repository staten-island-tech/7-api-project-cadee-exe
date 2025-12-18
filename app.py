

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

# pokemon = getPoke("umbreon")
# print(pokemon)     

import requests

def getOperator(operator):
    url = "https://api.rhodesapi.com/api/operator"
    params= {
        "race": "sarkaz",
        "class": "guard",
        "tags": f"dps,{operator.lower()}"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Nothing")
        return None

    data = response.json()
    print(data)
    return data["data"] 

operator = getOperator("guard")
print(operator)      

get()

import tkinter
tk = tkinter
