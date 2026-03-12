class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                result += sign * num
                sign = 1
                num = 0
            elif c == "-":
                result += sign * num
                sign = -1
                num = 0
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        return result + sign * num