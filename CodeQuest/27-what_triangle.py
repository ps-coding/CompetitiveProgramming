import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    n1, n2, n3 = map(int, sys.stdin.readline().rstrip().split(", "))

    max_side = max(n1, n2, n3)

    if max_side >= (n1 + n2 + n3 - max_side):
        print("Not a Triangle")
    elif n1 == n2 == n3:
        print("Equilateral")
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print("Isosceles")
    else:
        print("Scalene")
