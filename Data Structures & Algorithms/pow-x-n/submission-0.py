class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        for i in range(n if n > 0 else -n):
            res *= x
        return res if n > 0 else (float(1) / res)