class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        product1, product2 = 1, 1
        for i in range(len(nums)):
            product1 *= nums[i]
            product2 *= nums[-i - 1]
            arr1.append(product1)
            arr2.append(product2)
        arr = []
        arr.append(arr2[-2])
        if len(nums) == 2:
            return [nums[1], nums[0]]
        for i in range(1, len(nums) - 1):
            arr.append(arr1[i - 1] * arr2[-i - 2])
        arr.append(arr1[i])
        return arr