class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sorted = sorted(zip(position, speed), reverse = True)
        num_fleet = len(position)
        time_remaining_prev = 0
        stack = []
        for pos, spd in cars_sorted:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)