import json
import os

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), "")
# os.system("clear")
print("-------------------------")
# ? Достаьть инфу из json
with open(c + "enter.json", encoding="utf8") as file:
    skin = json.load(file)
    # print(len(skin))
    
    file1 = open(c+ "exit.csv", "w", encoding="UTF-8")
    cou = 0
    c = []
    
    with open('first.txt', 'w', encoding="utf-8") as f:
        for node in skin:
            # print(node["text"])
            f.write(node["text"])
            f.write("\n")
        # c.append(node["Food"]["food"])
        # cou += 1
        # if node["gameId"] == 17 and node["id"] == 3059:
        #     c.append(node["groupKey"])


# print(cou)
# print(set(c))
# print(len(set(c)))
