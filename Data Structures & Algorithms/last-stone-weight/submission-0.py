class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for i in range(len(stones)):
            arr.append(-stones[i])
        heapq.heapify(arr)
        while arr:
            x = -heapq.heappop(arr)
            if arr:
                y = -heapq.heappop(arr)
            else:
                return x
            
            if x != y:
                heapq.heappush(arr, min(x,y) - max(x,y))
        return 0