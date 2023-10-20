import math


def sin_table():
    print("sin(x)\t\tx")
    for i in range(0, 1001, 1):
        print("%2.6f %2.6f" % (math.sin(0 + i * (2 * math.pi / 1000)), (i * (2 * math.pi / 1000))))


def main():
    sin_table()


if __name__ == '__main__':
    main()
