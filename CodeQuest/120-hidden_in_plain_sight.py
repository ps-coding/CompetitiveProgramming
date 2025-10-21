import sys


def solve(words):
    ans = ""
    for word, index in words:
        ans += word[index]

    print(ans)


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    words = []
    numWords = int(sys.stdin.readline().rstrip())
    for _ in range(numWords):
        word, index = sys.stdin.readline().rstrip().split("|")
        words.append((word, int(index)))
    solve(words)
