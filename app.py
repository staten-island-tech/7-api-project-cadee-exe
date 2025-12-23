

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

# import requests

# def getOperator(operator):
#     url = f"https://awedtan.ca/api/operator/exusiai{operator.lower()}"
#     response = requests.get(url)

#     if response.status_code != 200:
#         print("Nothing")
#         return None

#     data = response.json()

#     params = {
#         "name": data.get("name"),
#         "archetype": data.get("archetype")
#     }

#     return params

# operator = getOperator("char_103_angel")
# print(operator)



import requests

def getOperator(operator):
    url = f"https://awedtan.ca/api/operator/{operator.lower()}"
    response = requests.get(url)

    print("Status:", response.status_code)

    if response.status_code != 200:
        print("Request failed")
        return None

    data = response.json()
    print("Data:", data)

    if "name" not in data or "archetype" not in data:
        print("Expected keys not found")
        return None

    return {
        "name": data["{name}"],
        "archetype": data["{archetype}"]
    }

operator = getOperator("69447ee8d7ac17dee8d7b5a0")
print("Result:", operator)