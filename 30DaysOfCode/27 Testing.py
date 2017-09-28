import random

print('5')
i = 1
while i < 6:
    n = random.randint(3, 200)
    k = random.randint(1, n)
    print(str(n) + ' ' + str(k))
    if i in (1, 3 , 5):
        A = '0'
        a = 0
        for a in range(k-2):
            A = A + ' ' + str(random.randint(-10**3, -1))
            a += 1
        b = 0
        for b in range(n-a-1):
            A = A + ' ' + str(random.randint(0, 10**3))
            b += 1
        print(A)

    else:
        A = '0'
        a = 0
        for a in range(k-2):
            A = A + ' ' + str(random.randint(0, 10**3))
            a += 1
        b = 0
        for b in range(n-a-1):
            A = A + ' ' + str(random.randint(-10**3, -1))
            b += 1
        print(A)
    i += 1
