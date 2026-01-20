import sys


class Data:
    def __init__(self, year: int, income: int):
        self.year = year
        self.income = income


def solve(country, data: list[Data]):
    print(f"{country}:")

    data.sort(key=lambda x: x.year)

    for point in data:
        print(f"{point.year}", end=" ")
        for _ in range(point.income):
            print("*", end="")
        print()


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    country = sys.stdin.readline().rstrip()
    dataPoints = []
    numDataPoints = int(sys.stdin.readline().rstrip())
    for _ in range(numDataPoints):
        income, year = sys.stdin.readline().rstrip().split(" ")
        income = round(float(income) / 1000)
        year = int(year)
        dataPoints.append(Data(year, income))
    solve(country, dataPoints)
