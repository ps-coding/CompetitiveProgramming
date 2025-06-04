import sys


class Triangulate:
    def __init__(self, x1, y1, d1, x2, y2, d2, x3, y3, d3):
        self.a = (x1, y1, d1)
        self.b = (x2, y2, d2)
        self.c = (x3, y3, d3)

    def solve(self) -> tuple[int, int]:
        first = set()
        second = set()
        third = set()

        x = 0

        while x <= self.a[2]:
            first.add((self.a[0] + x, self.a[1] + (self.a[2] - x)))
            first.add((self.a[0] - x, self.a[1] + (self.a[2] - x)))
            first.add((self.a[0] + x, self.a[1] - (self.a[2] - x)))
            first.add((self.a[0] - x, self.a[1] - (self.a[2] - x)))
            x += 1

        x = 0

        while x <= self.b[2]:
            second.add((self.b[0] + x, self.b[1] + (self.b[2] - x)))
            second.add((self.b[0] - x, self.b[1] + (self.b[2] - x)))
            second.add((self.b[0] + x, self.b[1] - (self.b[2] - x)))
            second.add((self.b[0] - x, self.b[1] - (self.b[2] - x)))
            x += 1

        x = 0

        while x <= self.c[2]:
            third.add((self.c[0] + x, self.c[1] + (self.c[2] - x)))
            third.add((self.c[0] - x, self.c[1] + (self.c[2] - x)))
            third.add((self.c[0] + x, self.c[1] - (self.c[2] - x)))
            third.add((self.c[0] - x, self.c[1] - (self.c[2] - x)))
            x += 1

        return (first.intersection(second).intersection(third)).pop()


def solve(prob: Triangulate):
    print(f"({prob.solve()[0]},{prob.solve()[1]})")


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    x1, y1, d1, x2, y2, d2, x3, y3, d3 = sys.stdin.readline().rstrip().split(" ")
    x1 = int(x1)
    y1 = int(y1)
    d1 = int(d1)
    x2 = int(x2)
    y2 = int(y2)
    d2 = int(d2)
    x3 = int(x3)
    y3 = int(y3)
    d3 = int(d3)
    solve(Triangulate(x1, y1, d1, x2, y2, d2, x3, y3, d3))
