class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m, n = piles[0], piles[0]
        if len(piles) == 1:
            return piles[0] // h if piles[0] % h == 0 else piles[0] // h + 1
        for i in range(len(piles)):
            if piles[i] < m:
                m = piles[i]
            if piles[i] > n:
                n = piles[i]

        l, r = 1, n
        while l < r:
            total = 0
            k = l + ((r - l) // 2) 
            for i in range(len(piles)):
                if piles[i] % k != 0:
                    total += piles[i] // k + 1
                else:
                    total += piles[i] // k
            if total <= h:
                r = k
            else:
                l = k + 1
        return l
            

            
                