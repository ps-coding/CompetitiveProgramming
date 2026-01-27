import sys

import math


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def solve(budgetedCosts, actualCosts, numItems):
    sum = 0
    for i in range(numItems):
        sum += float(actualCosts[i]) - float(budgetedCosts[i])
    return sum / numItems


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    numItems = int(sys.stdin.readline().rstrip())
    budgetedCosts = sys.stdin.readline().rstrip().split(" ")
    actualCosts = sys.stdin.readline().rstrip().split(" ")
    print(f"{(normal_round(solve(budgetedCosts, actualCosts, numItems))):.2f}")
