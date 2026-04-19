class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        maxLen = 0
        curr_left = 0
        for i in range(len(s)):
            while s[i] in curr:
                curr.remove(s[curr_left])
                curr_left += 1
            curr.add(s[i])
            maxLen = max(maxLen, i - curr_left + 1)
        return maxLen