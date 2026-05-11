class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) + 1
        result = []
        for i in range(n-k):
            window = nums[i:i+k]
            result.append(max(window))
        return result