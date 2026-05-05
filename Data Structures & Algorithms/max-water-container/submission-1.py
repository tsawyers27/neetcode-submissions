class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_height = 0
        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            if water > max_height:
                max_height = water
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
        return max_height