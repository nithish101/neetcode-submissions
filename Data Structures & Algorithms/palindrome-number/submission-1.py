class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10
        for i in range(len(digits) // 2):
            if digits[i] != digits[-1 - i]:
                return False
        return True