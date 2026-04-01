class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0

        for num in nums:
            if not (num - 1) in setNums:
                length = 1
                while (num + length) in setNums:
                    length += 1
                res = max(length, res)
        return res
        