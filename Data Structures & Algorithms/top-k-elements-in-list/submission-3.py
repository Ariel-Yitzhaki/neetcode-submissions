class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        arr = []
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        topk = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)
        for (k, n) in topk[:k]:
            arr.append(k)
        return arr
