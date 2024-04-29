class FourCal:
    def __init__(self, a=0, b=0):
        self.result = 0
        self.data = (a, b)

    def setdata(self, a, b):
        self.data = (a, b)

    def add(self):
        self.result = self.data[0] + self.data[1]
        return self.result

    def sub(self):
        self.result = self.data[0] - self.data[1]
        return self.result

    def mul(self):
        self.result = self.data[0] * self.data[1]
        return self.result

    def div(self):
        self.result = self.data[0] / self.data[1]
        return self.result


class MoreFourCal(FourCal):
    def pow(self):
        self.result = self.data[0] ** self.data[1]
        return self.result


class SafeFourCal(FourCal):
    def div(self):
        if self.data[1] == 0:
            return "NaN"
        else:
            self.result = self.data[0] / self.data[1]
            return self.result


class Family:
    lastname = "Kim"


if __name__ == '__main__':
    print(Family.lastname)

    a = Family()
    b = Family()
    print(a.lastname, b.lastname, end=" ",)
    print()

    Family.lastname = "Park"
    print(a.lastname, b.lastname, end=" ")