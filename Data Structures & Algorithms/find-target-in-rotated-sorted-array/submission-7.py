class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            # in the right part of the split
            if target <= nums[r-1]:
                if nums[m] < target :
                    l = m + 1
                elif nums[m] > target:
                    if nums[m] <= nums[r - 1]:
                        r = m
                    elif nums[m] > nums[r - 1]:
                        l = m + 1
                else:
                    return m
            else:
                if nums[m] < target and nums[m] > nums[l]:
                    l = m + 1                    
                elif nums[m] == target:
                    return m
                else:
                    r = m
               
        
        return -1
                    
