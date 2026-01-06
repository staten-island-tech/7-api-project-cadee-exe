

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
    url = f"https://api.rhodesapi.com/api/operator/ines"
    response = requests.get(url)

    print("Status:", response.status_code)

    if response.status_code != 200:
        print("Request failed")
        return None

    data = response.json()
    print("Data:", data)

    if "name" not in data or "archetype" not in data:
        print("Not in data")
        return None

    return {
        "name": data["name"],
        "rarity": data["rarity"]
    }

operator = getOperator("Ines")
print(operator)


import tkinter as tk
import random

def random_color():
    return "#{:02x}{:02x}{:02x}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def generate_palette():
    for box, label in zip(color_boxes, color_labels):
        color = random_color()
        box.config(bg=color)
        label.config(text=color)

def copy_to_clipboard(color):
    root.clipboard_clear()
    root.clipboard_append(color)
    root.update()

root = tk.Tk()
root.title("Color Palette Maker")
root.geometry("500x300")
root.resizable(False, False)

title = tk.Label(root, text="Color Palette", font=("Comic Sans", 16, "bold"))
title.pack(pady=10)

palette_frame = tk.Frame(root)
palette_frame.pack(pady=10)

color_boxes = []
color_labels = []

for i in range(5):
    frame = tk.Frame(palette_frame)
    frame.grid(row=0, column=i, padx=5)

    box = tk.Label(frame, bg="white", width=10, height=5, relief="ridge")
    box.pack()

    label = tk.Label(frame, text="#a6ff00", font=("Comic Sans", 10))
    label.pack()

    box.bind("<Button-1>", lambda e, l=label: copy_to_clipboard(l.cget("text")))

    color_boxes.append(box)
    color_labels.append(label)

generate_btn = tk.Button(
    root,
    text="Generate Palette",
    font=("Comic Sans", 12),
    command=generate_palette
)
generate_btn.pack(pady=10)

generate_palette()
root.mainloop()

