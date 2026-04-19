class Solution:
    def getSum(self, a: int, b: int) -> int:
        total = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            curr = a_bit ^ b_bit ^ carry
            carry = 1 if a_bit + b_bit + carry >= 2 else 0
            total |= (curr << i)

        if total > 0x7FFFFFFF:
            total = ~(total ^ 0xFFFFFFFF)

        return total