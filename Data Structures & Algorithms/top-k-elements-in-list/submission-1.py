class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts.keys():
                counts[n] += 1
            else:
                counts[n] = 1
        result = []
        for x in range(k):
            best_key = 0
            best_value = 0
            for key, value in counts.items():
                if value > best_value:
                    best_value = value
                    best_key = key
            result.append(best_key)
            counts[best_key] = 0
        return result