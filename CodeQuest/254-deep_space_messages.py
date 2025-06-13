import sys


def decode(text: str):
    curr_num = 0
    ans = ""

    for char in text:
        if char.isdigit():
            n = int(char)
            curr_num = curr_num * 10 + n
        else:
            if curr_num != 0:
                char = chr(curr_num + 64)
                ans += char
            curr_num = 0

    if curr_num != 0:
        char = chr(curr_num + 64)
        ans += char

    return ans


cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    text = sys.stdin.readline().rstrip()
    print(decode(text).lower())
