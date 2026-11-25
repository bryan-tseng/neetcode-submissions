class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for x in num_set:
            if x - 1 not in num_set:
                length = 1
                curr = x
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest