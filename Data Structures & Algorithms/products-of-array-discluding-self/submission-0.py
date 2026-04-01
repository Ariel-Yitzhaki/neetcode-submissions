class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        arr = []
        zero_counter = []
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                zero_counter.append(i)
        length = len(zero_counter)
        for i in range(len(nums)):
            if length == 0:
                arr.append(product // nums[i])
            elif length > 1:
                arr.append(0)
            else:
                if nums[i] != 0:
                    arr.append(0)
                else:
                    arr.append(product)     
            
        return arr