def need(x):
    m = []
    for i in range(1, int(x ** 0.5) + 1):
        if x == i * i:
            if i % 2 == 0:
                m += [i]
        elif x % i == 0:
            if i % 2 == 0:
                m += [i]
            if (x // i) % 2 == 0:
                m += [x // i]
    return m

for num in range(110203, 110246):
    answ = need(num)
    if len(answ) == 4:
        answ.sort()
        print(answ)
