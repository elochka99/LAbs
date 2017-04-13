# Горохова Елена КНИТ 16-А
import numpy as np
import random
def bubble_sort(A):
    ''' Cортировка пузырьком

        работает с помощью обмена двух соседних элементов до правиьной сортировки
        в худшем случае требует O(N**2) времени, О(1) памяти, O(N**2) обменов. Сортировка является устойчивой '''
    N = len(A)
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(N-i-1):
            if (A[j] > A[j+1]):
                tmp = A[j]
                A[j] = A[j+1]
                A[j + 1] = tmp
                flag = True
        i+=1
    return A
def selection_sort(A):
    ''' Cортировка выбором.

        работает с помощью выбора наименьшего элемента и переносит его вначало массива (к отсортированной части)
        до получения правильной сортировки
        в худшем случае требует O(N**2) времени, О(1) памяти, O(N) обменов. Сортировка является не устойчивой '''
    N = len(A)
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if A[j] < A[min]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
    return A
def insertion_sort(A):
    ''' Cортировка вставками.

        работает с помощью изьятия наименьшего элемента (присваивается в переменную) и переносит его
        к отсортированной части, работает до получения правильной сортировки
        в худшем случае требует O(N**2) времени, О(1) памяти, O(N**2) обменов. Сортировка является устойчивой '''
    N = len(A)
    for i in range(1,N):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
def cocktail_sort(A):
    ''' Cортировка перемешиванием.

        если при движении по части массива перестановки не происходят, то эта часть массива уже отсортирована и,
        ледовательно, её можно исключить из рассмотрения.
        Дальше при движении от конца массива к началу минимальный элемент «всплывает» на первую позицию, а максимальный
        элемент сдвигается только на одну позицию вправо.
        Эти две идеи приводят к следующим модификациям в методе пузырьковой сортировки. Границы рабочей части массива
        (то есть части массива, где происходит движение) устанавливаются в месте последнего обмена на каждой итерации.
        Массив просматривается поочередно справа налево и слева направо.
        Лучший случай для этой сортировки по времени — отсортированный массив O(n),
        худший — отсортированный в обратном порядке O(n**2).
        Наименьшее число сравнений в алгоритме Шейкер-сортировки C=N-1.
        Это соответствует единственному проходу по упорядоченному массиву (лучший случай)
        СЛОЖНОСТЬ ПО ПАМЯТИ	ОБЩАЯ = O(n), ДОПОЛНИТЕЛЬНАЯ = O(1)
        Устойчивая сортировка'''
    N = range(len(A) - 1)
    while True:
        for j in (N, reversed(N)):
            flag = False
            for i in j:
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    flag = True
            if not flag:
                return A
def shell_sort(d):
    ''' Сортировка перемешиванием.

    Сортируем вставкой подгруппы элементов, но только в подгруппе они идут не в ряд, а равномерно выбираются
     с некоторой дельтой по индексу. После первоначальных грубых проходов, дельта методично уменьшается,
     пока расстояние между элементами этих несвязных подмножеств не достигнет единицы.
      Благодаря первоначальным проходам с большим шагом, большинство малых по значению элементов
      перебрасываются в левую часть массива, большинство крупных элементов массива попадают в правую.
      СЛОЖНОСТЬ ПО ВРЕМЕНИ	ХУДШАЯ  - Зависит от шага, ЛУЧШАЯ =	O(n)
    СЛОЖНОСТЬ ПО ПАМЯТИ	ОБЩАЯ =	O(n), ДОПОЛНИТЕЛЬНАЯ =	O(1)
    Сортировка не устойчивая
    '''
    n = len(d)
    while True:
        n = n//2
        for i in range (n, len(d), n):
            k = i
            while k>0 and d[k] < d[k-n]:
                d[k], d[k-n] = d[k-n], d[k]
                k = k - n
        if n ==  1:
            break
    return d
def heap_sort(li):
    ''' Пирамидальная сортировка.

    работает в худшем, в среднем и в лучшем случае (то есть гарантированно) за О(n log n) операций
    при сортировке n элементов. Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1)).
    Может рассматриваться как усовершенствованная сортировка пузырьком,
    в которой элемент всплывает (min-heap) / тонет (max-heap) по многим путям.
    '''
    def down_Heap(li, k, n):
        '''
        Функция создает бинарное сортировочное дерево

        где li - начальный элемент, k - конечный элемент, n - сам массив
        '''
        new_elem = li[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and li[child] < li[child+1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(size//2-1,-1,-1):
        down_Heap(li, i, size)
    for i in range(size-1,0,-1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        down_Heap(li, 0, i)
    return li
print('Как Вы хотите вводить информацию в БД: вручную или рандомно? [1/2]')
while True:
    try:
        ask_inp = int(input('Выберите цифру → '))
        n = int(input("введите кол во элeментов в массиве: "))
        A = np.zeros(n, dtype=int)
        if ask_inp == 1:
            for j in range(n):
                A[j] = int(input("Заполните матрицу: "))
        elif ask_inp == 2:
            for j in range(n):
                A[j] = random.randint(0, 100000)
        else:
            print('Пожалуйста, введите корректные данные ☻\n')
            continue
        print("ваша последовательность чисел: ", A)
        break
    except ValueError:
        print('Пожалуйста, введите целое число ☻\n')
        continue
print('Каким методом сортировать? \n[1 - bubble / 2 - selection / 3 - insertion / 4 - cocktail / 5 - shell / 6 - heapsort ]')
while True:
    try:
        ask = int(input('Выберите цифру → '))
        if ask == 1:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность bubble_sort по возрастанию: ", bubble_sort(A))
            elif order == "2":
                print("отсортированная последовательность bubble_sort по убыванию: ", bubble_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        elif ask == 2:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность selection_sort по возрастанию: ", selection_sort(A))
            elif order == "2":
                print("отсортированная последовательность selection_sort по убыванию: ", selection_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        elif ask == 3:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность insertion_sort по возрастанию: ", insertion_sort(A))
            elif order == "2":
                print("отсортированная последовательность insertion_sort по убыванию: ", insertion_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        elif ask == 4:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность cocktail_sort по возрастанию: ", cocktail_sort(A))
            elif order == "2":
                print("отсортированная последовательность cocktail_sort по убыванию: ", cocktail_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        elif ask == 5:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность shell_sort по возрастанию: ", shell_sort(A))
            elif order == "2":
                print("отсортированная последовательность shell_sort по убыванию: ", shell_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        elif ask == 6:
            order = input("1 - по возростанию \ 2 - в порядке убывания :")
            if order == "1":
                print("отсортированная последовательность heap_sort по возрастанию: ", heap_sort(A))
            elif order == "2":
                print("отсортированная последовательность heap_sort по убыванию: ", heap_sort(-A) * -1)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
        else:
            print('Пожалуйста, введите корректные данные ☻\n')
            continue
    except ValueError:
        print('Пожалуйста, введите целое число ☻\n')
        continue

