class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for idx, i in enumerate(nums):
            if target-i in mp:
                return [mp[target-i], idx]
            mp[i] = idx
        return [-1,-1]