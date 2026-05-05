class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, x in enumerate(nums):
            left = 0
            right = len(nums)-1
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                tmp = nums[left] + nums[right]
                if tmp == -x:
                    new_elem = [nums[i], nums[left], nums[right]]
                    new_elem.sort()
                    if new_elem in result:
                        left += 1
                        continue
                    else:
                        result.append(new_elem)
                        left += 1
                elif tmp != -x:
                    if tmp < -x:
                        left += 1
                    elif tmp > -x:
                        right -= 1
        return result