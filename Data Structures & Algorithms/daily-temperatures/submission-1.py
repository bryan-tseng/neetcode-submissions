class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i, daily_temp in enumerate(temperatures):
            while stack != [] and daily_temp > temperatures[stack[-1]]:
                j = stack.pop()
                results[j] = i - j
            stack.append(i)
        return results