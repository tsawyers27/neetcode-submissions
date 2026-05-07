class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        maxLength = 0
        if len(s) == 1:
            return 1
        while right <= len(s):
            test = set(s[left:right])
            if len(test) == len(s[left:right]):
                right += 1
            elif len(test) < len(s[left:right]):
                left += 1
            maxLength = max(maxLength, (right - left) - 1)
        return maxLength