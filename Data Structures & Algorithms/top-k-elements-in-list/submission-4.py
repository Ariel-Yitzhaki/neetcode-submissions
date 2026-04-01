class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            d[n] = d.get(n, 0) + 1
        for n, cnt in d.items():
            bucket[cnt].append(n)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
