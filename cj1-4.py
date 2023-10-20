class favAnimal:
    def __init__(self, armLen, legLen, eyesNum, tail, furry):
        self.armLen = float(armLen)
        self.legLen = float(legLen)
        self.eyesNum = int(eyesNum)
        self.tail = bool(tail)
        self.furry = bool(furry)

    def __str__(self):
        return f'Favorite animal has the following features arm length: {self.armLen} in, leg length: {self.legLen} in, number of eyes: {self.eyesNum}, has tail: {self.tail}, is furry: {self.furry}'


def main():
    a = favAnimal(2.2910, 10, 3, True, False)
    print(a)


if __name__ == '__main__':
    main()
