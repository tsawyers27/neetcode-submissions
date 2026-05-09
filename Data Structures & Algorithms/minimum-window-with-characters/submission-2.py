class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        left = 0
        right = 1
        t_counts = Counter(t)
        while left < right and right <= len(s):
            window = s[left:right]
            test_counts = Counter(window)
            if t_counts <= test_counts:
                if result == "":
                    result = window
                else:
                    if len(window) <= len(result):
                        result = window
                        left += 1
                    elif len(window) > len(result):
                        left +=1
                    else:
                        right += 1
            else:
                right += 1


        return result
