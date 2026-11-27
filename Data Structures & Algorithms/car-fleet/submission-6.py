class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sorted = sorted(zip(position, speed), reverse = True)
        stack = []
        for position, speed in cars_sorted:
            stack.append((target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
