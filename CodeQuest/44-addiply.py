import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    n1, n2 = sys.stdin.readline().rstrip().split(" ")
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2, end=" ")
    print(n1 * n2)
