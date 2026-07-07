class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [x[0] for x in sorted(Counter(nums).items(), key=lambda x: x[1]) if x[1] > n//3]