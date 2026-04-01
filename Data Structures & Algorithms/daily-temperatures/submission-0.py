class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, ind = stack.pop()
                result[ind] = i - ind
            stack.append((temperatures[i], i))
        return result