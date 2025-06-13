import sys
import re


def isValid(text):
    exps = [
        r".*'; .* --.*",
        r".*\$\{.*\}.*",
        r".*\$\(.*\).*",
        r".*&& sudo.*",
        r".*&& su -.*",
        r".*;;.*",
        r".*%s.*",
        r".*%x.*",
        r".*%n.*",
    ]
    exps_case_ins = [".*' OR 1=1.*", ".*<script.*"]

    for exp in exps:
        if re.match(exp, text, flags=re.DOTALL) is not None:
            return False

    for exp in exps_case_ins:
        if re.match(exp, text, flags=re.DOTALL | re.IGNORECASE):
            return False

    return True


cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    text = sys.stdin.readline().rstrip()
    if isValid(text):
        print(text)
    else:
        print("REJECTED")
