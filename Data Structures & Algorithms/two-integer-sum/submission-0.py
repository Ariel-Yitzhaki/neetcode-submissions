class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(lambda: -1)
        hashmap[nums[0]] = 0
        for i in range(1, len(nums)):
            n = target - nums[i]
            if hashmap[n] != -1:
                return [hashmap[n], i]
            hashmap[nums[i]] = i
       