import requests

def getOperator(Operator):
    response = requests.get(f"https://awedtan.ca/api/operator/hellagur{Operator.lower()}")
    if response.status_code != 200:
        print("error getting data srry")
        return "sorry, either operator doesnt exist or trouble fetching data"
    
    data = response.json()
    return{
        "name": data["name"],
        "class": data["class"],
        "archetype": data["archetype"],
        "skills": data["skills"],
        "traits": data["traits"],
        "class": [c["class"]["operator"] for c in data["class"]]
    }
operator = getOperator("Amiya")
print(operator)