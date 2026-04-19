class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount = {}
        for c in s:
            if c in charCount:
                charCount[c] += 1
            else:
                charCount[c] = 1
        for c in t:
            if c in charCount:
                if (charCount[c] <= 0):
                    return False
                else:
                    charCount[c] -= 1
            else:
                return False
        return True
        