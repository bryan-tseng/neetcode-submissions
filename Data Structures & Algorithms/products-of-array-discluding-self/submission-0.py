class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        before_cumulative = 1
        for i in range(n):
            ans[i] *= before_cumulative
            before_cumulative *= nums[i]
        after_cumulative = 1
        for i in range(n-1, -1, -1):
            ans[i] *= after_cumulative
            after_cumulative *= nums[i]
        return ans