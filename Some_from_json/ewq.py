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
    
    for node in skin:
        # print(node)
        c.append(node["Food"]["food"])
        cou += 1
        # if node["gameId"] == 17 and node["id"] == 3059:
        #     c.append(node["groupKey"])

print(cou)
print(set(c))
print(len(set(c)))

# {'aamakarov', 'pes_pif', 'TerTro', 'serejanin', 'mamamia4s', 'Khenntaar', 'irrra13', 'tyalina', 'Qayss1', None}

# {480003, 480005, 430099, 430100, 450195, 430999, 451995, 430499, 440099, 440100, 440999, 461995, 430003, 440499, 430005, 450995, 430010, 471995, 430399, 450495, 460995, 430020, 440005, 440010, 440399, 460495, 454995, 440020, 470995, 430299, 459995, 430049, 464995, 440299, 469995, 440049, 474995, 479995}

# {530049, 564995, 540299, 569995, 540049, 574995, 579995, 580003, 580005, 530099, 530100, 550195, 530999, 551995, 530499, 540099, 540100, 559995, 540999, 561995, 530003, 540499, 530005, 550995, 530010, 571995, 530399, 550495, 560995, 530020, 540005, 540010, 540399, 560495, 554995, 540020, 570995, 530299}

# {644995, 630020, 660995, 620299, 649995, 620049, 654995, 630299, 659995, 630049, 664995, 669995, 620099, 620100, 640195, 620999, 641995, 610003, 620499, 610005, 630099, 630100, 630999, 651995, 620003, 630499, 620005, 640995, 650495, 620010, 661995, 620399, 640495, 650995, 620020, 630005, 630010, 630399}

# 9059, 49059, 5059, 1995059, 4995059, 19059, 3059, 99059, 199059, 299059, 399059, 499059, 999059, 195059, 495059, 9995059, 995059