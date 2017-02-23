#Gorokhova Olena KNIT 16-A
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из
# пяти 12-летних подциклов. Подциклы обозначались названиями цвета: зелёный,
# красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
# названия животных: крысы, коровы, тигра, зайца, драковна, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) --
# начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.
k = True
while k:
    import random
    from enum import Enum
    class color(Enum):
        White = 1
        Yellow = 2
        Black = 3
        Green = 4
        Red = 0
    class animal(Enum):
        Rat = 1984
        Cow = 1985
        Tiger = 1986
        Rabbit = 1987
        Dragon = 1988
        Snake = 1989
        Hourse = 1990
        Sheep = 1991
        Monkey = 1992
        Chicken = 1993
        Dog = 1994
        Pig = 1995
    i = int(input("введите год:"))
    n = h = i
    b = range(1984, 1996)
    if i < 1984:
        while i not in b:
            i += 12
    elif i > 1995:
        while i not in b:
            i -= 12
    if n >= 0:
        n %= 5
    else:
        print('год не входит в нашу эру')
    print(h,'-',color(n).name, animal(i).name)