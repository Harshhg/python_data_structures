def coin(n, ar):
    for x in ar:
        if (n - x > 0):
            print(x, end=" ")
            break
        elif (n - x == 0):
            print(x, end=" ")
            return
    coin(n - x, ar)

ar = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
coin(int(input()), ar)
