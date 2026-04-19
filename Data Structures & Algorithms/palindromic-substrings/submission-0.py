class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i, c in enumerate(s):
            #check odd
            i1 = i
            i2 = i
            while(i1 >= 0 and i2 < len(s)):
                if s[i1] == s[i2]:
                    count += 1
                    i1 -= 1
                    i2 += 1
                else:
                    break
            #check even
            i1 = i
            i2 = i + 1
            while(i1 >= 0 and i2 < len(s)):
                if s[i1] == s[i2]:
                    count += 1
                    i1 -= 1
                    i2 += 1
                else:
                    break

        return count