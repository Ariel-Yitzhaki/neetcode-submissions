class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        
        if nums[0] < nums[r - 1] or r == 1:
            return nums[0]

        while l < r- 1:
            m = l + ((r - l) // 2)
            if nums[m] >= nums[l] and nums[m] >= nums[r - 1]:
                l = m
            elif nums[m] < nums[l]:
                r = m
       
                
        
        return nums[l + 1]