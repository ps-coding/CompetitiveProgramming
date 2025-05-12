import sys


def solve(tickets):
    cityMap = {}
    firstCities = set()
    secondCities = set()

    for pair in tickets:
        city1, city2 = pair
        cityMap[city2] = city1
        firstCities.add(city1)
        secondCities.add(city2)

    currCity = (secondCities - firstCities).pop()

    while currCity is not None:
        print(currCity)
        currCity = cityMap.get(currCity)


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    tickets = []
    numTickets = int(sys.stdin.readline().rstrip())
    for ticketNum in range(numTickets):
        city1, city2 = sys.stdin.readline().rstrip().split(" ")
        tickets.append((city1, city2))
    solve(tickets)
