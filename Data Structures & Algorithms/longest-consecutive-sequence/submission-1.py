class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        curr, res, last = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == last+1:
                curr += 1
            else:
                curr = 1
            last = nums[i]
            
            res = max(curr, res)
        return res