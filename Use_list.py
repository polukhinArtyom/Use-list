print("*****Создаём список и выводим его на экран*****")
spacelist = ["rocket", "planet", "asteroid", "alien"]
print(spacelist[0])
print("**********Выводим на экран значения списка с помощью цикла*****")
for item in spacelist:
    print(item)
print("******Выводим на экран элементы цикла в строку******")
print(spacelist)
print("*********Заменяем элемент цикла и выводим на экран*****")
spacelist = ["rocket", "planet", "asteroid", "alien"]
spacelist[0] = "planet zarg"
for item in spacelist:
    print(item)
print("*********Удаляем первый элемент цикла и выводим на экран********")
spacelist = ["rocket", "planet", "asteroid", "alien"]
del spacelist[0]
for item in spacelist:
    print(item)
print("*******Добавление элемента в список*******")
spacelist = ["rocket", "planet", "asteroid", "alien"]
spacelist.append("moon")
print(spacelist)
print("*******Объединение списков*******")
spacelist1 = ["rocket", "planet", "asteroid", "alien"]
spacelist2 = ["spacestation", "star", "black hole"]
spacelist = spacelist1 + spacelist2
for item in spacelist:
    print(item)
