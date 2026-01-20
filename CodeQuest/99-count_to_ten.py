import sys


def solve(bits):
    for i in range(0, 2**bits):
        print(format(i, "b").zfill(bits))


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    bits = int(sys.stdin.readline().rstrip())
    solve(bits)
