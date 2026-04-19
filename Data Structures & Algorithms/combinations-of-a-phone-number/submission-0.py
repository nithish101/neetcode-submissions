class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        num_to_let = [['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']]

        def helper(prev, digits):
            if len(digits) == 0:
                return
            if len(digits) == 1:
                for n in num_to_let[int(digits[0]) - 2]:
                    answer.append(prev + n)
            for n in num_to_let[int(digits[0]) - 2]:
                    helper(prev + n, digits[1:])

        helper("", digits)
        return answer