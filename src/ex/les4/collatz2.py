import matplotlib.pyplot as plt

def Collatz (n: float) -> list[float]:

    numbers: list = [n]

    while n != 1:

        if n % 2 == 0:
            n = n / 2

        else:
            n = (3 * n) + 1

        numbers.append(n)

    return numbers

numbers: list[float] = Collatz(1000.0)

plt.plot(numbers)
plt.show()
