class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integers = []
        for n in tokens:
            if n not in ["+", "-", "*", "/"]:
                integers.append(int(n))
            else:
                b = integers.pop()
                a = integers.pop()
                if n == "+": integers.append(a + b)
                if n == "-": integers.append(a - b)
                if n == "*": integers.append(a * b)
                if n == "/": integers.append(int(a / b))
        return integers[-1]