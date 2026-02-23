class Solution:
    def myAtoi(self, s: str) -> int:

        int_min = -2**31
        int_max = 2**31 - 1
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (int_max - digit) // 10:
                return int_max if sign == 1 else int_min
            result = result * 10 + digit
            i += 1
        return sign * result