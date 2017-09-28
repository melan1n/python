Actual = input().split()
Da = int(Actual[0])
Ma = int(Actual[1])
Ya = int(Actual[2])
Expected = input().split()
De = int(Expected[0])
Me = int(Expected[1])
Ye = int(Expected[2])

fine = 0

if Ya - Ye > 0:
    fine = 10000

elif Ya == Ye:
    if Ma - Me > 0:
        fine = 500*(Ma - Me)
    elif Ma - Me < 0:
        fine = 0
    elif Ma - Me == 0:
        fine = 15*(Da - De)

print(str(fine))
