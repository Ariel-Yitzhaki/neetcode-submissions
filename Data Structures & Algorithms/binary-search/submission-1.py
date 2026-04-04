class Solution:
    def search(self, nums: List[int], target: int) -> int:
      
        r = len(nums)
        l = 0

        if nums[0] > target or nums[r - 1] < target:
            return -1
            
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] >= target:
                r = m
        return l if (l < len(nums) and nums[l] == target) else - 1  