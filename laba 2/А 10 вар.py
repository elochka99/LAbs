k=True
while k:
    v=set()
    n = 30
    print('введите', m, 'чисел :')
    while len(v) < n:
        try:
            v.add(int(input()))
            pass
        except ValueError:
            print("последовательность должна состоять из целых чисел")
    print("ваша последовательность :", v)
    m = min(v)
    M = max(v)
    print("минимальное число=", m, "максимальное число=", M)
    B = {i for i in range(m, M + 1)}
    print("числа которые не входят в последовательность:", B-v)
    a = input('Хотите продолжить? [y/n]: ')
    if a == 'y':
        continue
    else:
        break
