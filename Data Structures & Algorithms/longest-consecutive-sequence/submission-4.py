class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0

        setlist = set(nums)
        for num in setlist:
            if (num -1) not in setlist:
                length = 1
                while (num + length) in setlist:
                    length += 1
                long = max(length, long)
        return long