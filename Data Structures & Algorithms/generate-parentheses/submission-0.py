class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        stack = []

        def helper(o, c):
            if len(stack) == 2 * n:
                if o == c:
                    sol.append("".join(stack))
                return
            if o > c:
                stack.append(')')
                helper(o, c + 1)
                stack.pop()
            stack.append('(')
            helper(o + 1, c)
            stack.pop()

        helper(0, 0)
        return sol