import os

text = 'played: true' # фраза, которая будет дописана в конец строки
output = '' # инициализация результирующего текста
marker = 0

directory = "C:/Users\TeSoul\Documents\Obsidian Vault\Media DB\games"
 
# Получаем список файлов
files = os.listdir(directory)

def changein():
    output = ''
    for f in files:
        with open(directory + '/' + f, 'r', encoding="utf-8") as file:
            for line in file:
                if "gamesdb" in line:
                    output += line.replace("gamesdb", "mediaDB/game")
                    
                else:
                    output += line

        with open(directory + '/' + f, 'w', encoding="utf-8") as file:
            file.write(output)
        output = ''

def addin():
    # Выводим список файлов
    for f in files:
        with open(directory + '/' + f, 'r', encoding="utf-8") as file:
            for line in file: # считывание текущего файла
                if "tags" in line:
                    marker = 1

        if marker == 0:
            with open(directory + '/' + f, 'r', encoding="utf-8") as file:
                for line in file: # считывание текущего файла
                    if "Status" in line:
                        output += (text + '\n')
                    output += line
        if marker == 0:
            with open(directory + '/' + f, 'w', encoding="utf-8") as file:
                file.write(output)

        output = '' # инициализация результирующего текста
        marker = 0
        
changein()
# addin()

# Status: Done
# played: true