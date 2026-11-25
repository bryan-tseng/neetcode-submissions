class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        while front < back:
            diff = target - numbers[front]
            if diff == numbers[back]:
                return [front+1, back+1]
            if diff > numbers[back]:
                front += 1
            if diff < numbers[back]:
                back -= 1