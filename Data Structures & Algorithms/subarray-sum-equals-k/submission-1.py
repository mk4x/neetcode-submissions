from bisect import bisect_right, bisect_left

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum, subtract the other, hash the prefix sum to their location
        # get the target, count how many before the current index has that sum
        # use bin search to find the point of how many we need to search
        # then sum that all up

        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
                
        mp = defaultdict(list)
        for idx, num in enumerate(prefix):
            mp[num].append(idx)

        total = 0
        for idx, psum in enumerate(prefix):
            if psum-k in mp:
                added = bisect_left(mp[psum-k], idx)
                total += added
        
        return total


        
