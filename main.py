n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))
if n1 <= n2 and n1 <= n3:
    print (f"наименьшее числоn: {n1}")
elif n2 <= n1 and n2 <= n3:
    print(f"наименьшее число: {n2}")
elif n3 <= n1  and n3 <= n2:
    print(f"наименьшее число: {n3}")
else:
    print(f"all numbers equals")

    if n1 >= n2 and n1 >= n3:
        print(f"наибольшее числоn: {n1}")
    elif n2 >= n1 and n2 >= n3:
        print(f"наибольшее число: {n2}")
    elif n3 >= n1 and n3 >= n2:
        print(f"наибольшее число: {n3}")
    else:
        print(f"all numbers equals")

        average = (n1 + n2 + n3) / 3

meters = int(input("количество метров:"))
what = int(input("выберите меру измерения: мили - 1\т дюймі - 2\n ярды - 3"))
if what == 1:
    print(f"{meters} метров = meters*0.000621} миль")
elif what == 2:
    print(f"{meters} метров = {meters*39.37} дюймов")
elif what == 3:
    print(f"meters} метров = {meters*1.093613} ярдов")