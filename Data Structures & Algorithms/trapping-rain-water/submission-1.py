class Solution:
    def trap(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0
        while front < back:
            if height[front] < height[back]:
                max_left = max(max_left, height[front])
                total_water += max_left - height[front]
                front += 1
            else:
                max_right = max(max_right, height[back])
                total_water += max_right - height[back]
                back -= 1
        return total_water