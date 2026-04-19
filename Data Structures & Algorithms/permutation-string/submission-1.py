class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        one = [0] * 26
        two = [0] * 26
        matches = 0

        for i in range(len(s1)):
            one[ord(s1[i]) - ord('a')] += 1
            two[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if one[i] == two[i]:
                matches += 1

        l = 0
        r = len(s1)

        while r < len(s2):
            if matches == 26:
                return True
            l_ind = ord(s2[l]) - ord('a')
            r_ind = ord(s2[r]) - ord('a')
            if one[l_ind] == two[l_ind]:
                matches -= 1
            if one[r_ind] == two[r_ind]:
                matches -= 1
            two[l_ind] -= 1
            two[r_ind] += 1
            if one[l_ind] == two[l_ind]:
                matches += 1
            if one[r_ind] == two[r_ind]:
                matches += 1

            l += 1
            r += 1

        return matches == 26