class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        idxs = list(counts.most_common(k))
        result = []
        for elem in idxs:
            result.append(elem[0])
        return result