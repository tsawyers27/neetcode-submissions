class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            if n != 0:
                prod = math.prod(nums) / n
                result.append(int(prod))
            else:
                prod = 1
                for k, j in enumerate(nums):
                    if k != i:
                        prod = prod * j
                result.append(prod)
        return result