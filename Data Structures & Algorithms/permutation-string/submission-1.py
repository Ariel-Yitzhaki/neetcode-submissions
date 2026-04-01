class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = {}
        n = len(s1)
        if n > len(s2):
            return False
        for i in range(n):
            arr[s1[i]] = 1 + arr.get(s1[i], 0)
        
        l = 0
        
        while l + n - 1 < len(s2):
            if s2[l] in arr:
                temp = arr.copy()
                res = 1
                for i in range(n):
                    if s2[i + l] in temp:
                        temp[s2[i + l]] -= 1
                for s in temp:
                    if temp[s] != 0:
                        res = 0
                if res:
                    return True
            l += 1
        return False
                
            
                    
                

