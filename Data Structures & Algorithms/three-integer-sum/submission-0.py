class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = [] 
        l, r = 0, len(nums) - 1
        dic = {}
        temp = set()
        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                c = nums[i] + nums[j]
                if -c in dic and dic[-c] != i and dic[-c] != j:
                    key = tuple(sorted([nums[i], nums[j], -c]))
                    if key in temp:
                        continue
                    else:
                        arr.append(key)
                        temp.add(key)
        return arr
