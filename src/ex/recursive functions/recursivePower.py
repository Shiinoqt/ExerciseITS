def recursivePower(n:int, p:int) -> int:

    if p == 0:
        return 1

    else:
        return int(n * recursivePower(n, p-1))


print(recursivePower(3,4))