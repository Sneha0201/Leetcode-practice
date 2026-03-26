class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        addition = 0
        product = 1
        while temp > 0:
            r = temp % 10
            temp //= 10
            addition += r
            product *= r
        return product - addition