class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums).items()
        return [key for key, val in freq if val > n//3]