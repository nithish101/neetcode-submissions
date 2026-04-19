class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num *= 10
            num += d

        num += 1
        out = []
        while num > 0:
            out.insert(0, num % 10)
            num //= 10

        return out