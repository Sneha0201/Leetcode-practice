class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x != 0:
            digit = x % 10
            x = x // 10
            if result > int_max // 10:
                return 0
            result = result * 10 + digit
        result *= sign
        if result < int_min or result > int_max:
            return 0
        return result