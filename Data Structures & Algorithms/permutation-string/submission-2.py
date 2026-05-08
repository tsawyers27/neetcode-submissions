class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_counts = Counter(s1)
        n = len(s2)
        k = n - window_size
        for i in range(k+1):
            window = s2[i:i+window_size]
            window_counts = Counter(window)
            if s1_counts == window_counts:
                return True
        return False
