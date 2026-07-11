#To make palindrome one character can be deleted
s = "abdca"
def validPalindrome(s):
    def isPalindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return (isPalindrome(left + 1, right) or isPalindrome(left, right - 1))
        left += 1
        right -= 1
    return True
print(validPalindrome(s))