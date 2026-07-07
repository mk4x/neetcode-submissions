class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in sorted(Counter(nums).items(), key=lambda x: -x[1])[:k]]