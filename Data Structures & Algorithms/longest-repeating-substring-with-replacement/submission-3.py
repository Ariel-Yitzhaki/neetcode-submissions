class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = {}
        res = 0
        l = 0

        for r in range(len(s)):
            arr[s[r]] = 1 + arr.get(s[r], 0)

            while (r - l + 1) - max(arr.values()) > k:
                arr[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
                