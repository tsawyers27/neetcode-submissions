class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, x in enumerate(nums):
            if len(result) > 1:
                break
            for j, y in enumerate(nums):
                if i == j:
                    continue
                if x + y == target:
                    result.append(i)
                    result.append(j)
                    break
        return result