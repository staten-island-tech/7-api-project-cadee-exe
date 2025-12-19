

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
#     url = "https://api.rhodesapi.com/api/operator"
#     params= {
#         "race": "sarkaz",
#         "class": "guard",
#         "tags": f"dps,{operator.lower()}"
#     }

#     response = requests.get(url, params=params)

#     if response.status_code != 200:
#         print("Nothing")
#         return None

#     data = response.json()
#     print(data)
#     return data["data"] 

# operator = getOperator("guard")
# print(operator)      



import tkinter
tk = tkinter
# Create the main window (like your app's frame)
window = tk.Tk()
window.title("Message Reverser") # title at the top of the window
window.geometry("499x299") # set the size (width x height)
window.resizable(False, False) # keep it from being resized

prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
# Label to display the reversed message later
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)

# --- Functionality (what happens when you click the button) ---
def reverse_message():
    text = entry.get() # get whatever the user typed
    reversed_text = text[::-1] # slice trick to reverse a string
    result_label.config(text=f"Backwards: {reversed_text}")
# Button: when clicked, it calls reverse_message()
reverse_button = tk.Button(window, text="Reverse Message!",
font=("Arial", 14),

command=reverse_message)

reverse_button.pack(pady=10)
# Keeps the window open and waiting for clicks or typing
window.mainloop()
