class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        maxLength = 0

        while left < right and right <= len(s):
            window = s[left:right]
            maxChar = max(Counter(window).values())
            replacements = len(window) - maxChar
            if replacements <= k:
                right += 1
                if len(window) > maxLength:
                    maxLength += 1
            else:
                left += 1
        return maxLength