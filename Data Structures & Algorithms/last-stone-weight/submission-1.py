
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
       
        stones.sort()
        

        
        while len(stones) >1:
            h1 = stones.pop()
            h2 = stones.pop()

            if  h1 != h2 :
                heapq.heappush(stones , abs(h1 - h2))
            else :
                stones.append(0)
        return stones[0]
