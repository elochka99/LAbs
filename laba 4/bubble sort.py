import numpy as np
n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype = np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив: ", A)
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
    print(A)

