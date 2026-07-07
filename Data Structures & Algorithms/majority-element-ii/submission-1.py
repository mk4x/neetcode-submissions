class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [x[0] for x in Counter(nums).items() if x[1] > n//3]