class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        mostCommon = freq.most_common(k)

        return [num for num, freq in mostCommon]