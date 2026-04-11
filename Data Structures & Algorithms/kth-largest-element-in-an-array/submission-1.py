class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for i in range(n):
            if i >= k:
                heapq.heappushpop(heap, nums[i])
            else:
                heapq.heappush(heap, nums[i])
        return heap[0]