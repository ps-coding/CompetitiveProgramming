import sys

from decimal import Decimal, ROUND_HALF_UP


def solve(budgetedCosts, actualCosts, numItems):
    if numItems == 0:
        return Decimal(0)

    sum = Decimal(0)
    for i in range(numItems):
        sum += Decimal(actualCosts[i]) - Decimal(budgetedCosts[i])
    return sum / Decimal(numItems)


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    numItems = int(sys.stdin.readline().rstrip())
    budgetedCosts = sys.stdin.readline().rstrip().split(" ")
    actualCosts = sys.stdin.readline().rstrip().split(" ")
    print(
        f"{solve(budgetedCosts, actualCosts, numItems).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"
    )
