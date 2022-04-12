# Code Journal #1 - Prompt #5
import math
import numpy as np


def sinTable():
    x = np.linspace(0, 2 * math.pi, 1000)
    sinTable = []

    for i in x:
        sinTable.append([math.sin(i), i])

    sinArray = np.array(sinTable)
    return sinArray


def main():
    print(sinTable())


if __name__ == "__main__":
    main()
