class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                top = stack.pop()
                left = stack[-1] + 1 if stack else 0
                area = (i - left) * heights[top]
                if area > max_area:
                    max_area = area
            stack.append(i)
        return max_area