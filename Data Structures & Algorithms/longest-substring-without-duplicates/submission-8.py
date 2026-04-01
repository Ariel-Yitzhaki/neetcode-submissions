class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        res, l = 0, 0

        for i in range(len(s)):
            if s[i] in temp:
                l = max(temp[s[i]] + 1, l)
            temp[s[i]] = i
            res = max(res, i - l + 1)
            
        return res