import sys


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def invert(self):
        num = self.numerator
        self.numerator = self.denominator
        self.denominator = num

    def pop_whole(self) -> int:
        whole = self.numerator // self.denominator
        self.numerator -= whole * self.denominator
        return whole


def solve(frac: Fraction):
    count = 0
    answer = ""
    while count < 10:
        if frac.denominator == 0:
            break
        answer += str(frac.pop_whole()) + " "
        frac.invert()
        count += 1
    print(answer[0:-1])


numCases = int(sys.stdin.readline().rstrip())
for caseNum in range(numCases):
    predec, postdec = sys.stdin.readline().rstrip().split(".")
    num = int(predec) * 10 ** len(postdec) + int(postdec)
    den = 10 ** len(postdec)
    fraction = Fraction(num, den)
    solve(fraction)
