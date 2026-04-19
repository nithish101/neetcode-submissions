class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []

        for token in tokens:
            if token == "+" and len(temp) >= 2:
                s = temp[-2] + temp[-1]
                temp.pop()
                temp.pop()
                temp.append(s)
            elif token == "-" and len(temp) >= 2:
                s = temp[-2] - temp[-1]
                temp.pop()
                temp.pop()
                temp.append(s)
            elif token == "*" and len(temp) >= 2:
                s = temp[-2] * temp[-1]
                temp.pop()
                temp.pop()
                temp.append(s)
            elif token == "/" and len(temp) >= 2:
                s = int(temp[-2] / temp[-1])
                temp.pop()
                temp.pop()
                temp.append(s)
            else:
                temp.append(int(token))

        return temp[0]