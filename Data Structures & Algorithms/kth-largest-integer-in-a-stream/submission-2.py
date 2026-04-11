class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
     
        while len(nums) - k > 0:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) - self.k < 0:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        heapq.heappushpop(self.heap, val)
        return self.heap[0]
