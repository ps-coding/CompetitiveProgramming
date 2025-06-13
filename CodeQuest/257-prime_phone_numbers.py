import sys


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False

    return True


cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    text = sys.stdin.readline().rstrip()
    a = int(text[1:4])
    b = int(text[5:8])
    c = int(text[9:13])
    if coprime(a, b) and coprime(a, c) and coprime(b, c):
        print("TRUE")
    else:
        print("FALSE")
