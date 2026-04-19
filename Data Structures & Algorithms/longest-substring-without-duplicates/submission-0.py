class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        used = set(s[0])
        longest = 1
        beg = 0
        for i in range(1, len(s)):
            while s[i] in used:
                used.remove(s[beg])
                beg += 1
            used.add(s[i])
            longest = max(longest, len(used))

        return longest