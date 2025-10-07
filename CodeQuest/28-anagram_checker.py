import sys


def isPanagram(left, right):
    if left == right:
        return False

    counts = {}
    for i in left:
        counts[i] = counts.get(i, 0) + 1

    for i in right:
        counts[i] = counts.get(i, 0) - 1
        if counts[i] == 0:
            counts.pop(i)
        elif counts[i] < 0:
            return False

    if len(counts.keys()) != 0:
        return False

    return True


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    value = sys.stdin.readline().rstrip()
    left, right = value.split("|")

    if isPanagram(left, right):
        print(value + " = ANAGRAM")
    else:
        print(value + " = NOT AN ANAGRAM")
