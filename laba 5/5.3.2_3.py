# Горохова Елена КНИТ 16-А
# Дан некоторый текст,за которым следует точка. Программа определяет является ли текст правильной записью формулы,
# которая записана в сообтветствии с синтаксисом EBNF
znak = "+-*"
def text(t, p):
    '''
    Проверяет формулу рекурсивно
    :param t: параметр что передает текст формулы
    :param p: параметр что передает длину формулы
    :return: верная или не верная формула
    '''
    if p == -1:
        return True
    elif t[p] in znak:
        return t[p-1].isdigit() and text(t, p-1)
    elif t[p].isdigit():
        return t[p - 1] in znak and text(t, p-1)
    else:
        return False
def text_iter(t, p):
    '''
    Проверяет формулу итерационно
    :param t: параметр что передает текст формулы
    :param p: параметр что передает длину формулы
    :return: верная или не верная формула
    '''
    k = True
    for i in range(p, 1, -1):
        if not (t[p] in znak and t[p-1].isdigit()):
            k = False
            break
    return k
while True:
    try:
        t = input("Введите формулу: ")
        p = len(t)-1
        print("рекурсивно = ", text(t, p))
        print("Итерационно = ", text_iter(t, p))
    except ValueError:
        print("Введите коректные данные!")