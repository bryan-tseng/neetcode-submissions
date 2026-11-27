class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sorted = sorted(zip(position, speed), reverse = True)
        stack = []
        num_fleet = len(position)
        time_remaining_prev = 0
        for position, speed in cars_sorted:
            time_remaining = (target - position) / speed
            if time_remaining <= time_remaining_prev:
                num_fleet -= 1
            else:
                time_remaining_prev = time_remaining
        return num_fleet