class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        arr = []
        ind_track = []
        distance = 0
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            arr.append([distance, i])
            
        heapq.heapify(arr)
        temp = []
        for _ in range(k):
            ind = heapq.heappop(arr)
            print(points[ind[1]])
            temp.append(points[ind[1]])
        return temp