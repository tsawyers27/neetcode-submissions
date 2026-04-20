class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if i == j and idx1 != idx2:
                    return True
        return False