from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = []
        if nums.count(0) == 1:
            for i in nums:
                if i != 0:
                    total *= i
            for i in nums:
                if i == 0:
                    res.append(total)
                else:
                    res.append(0)
            return res
        elif nums.count(0) > 1:
            return [0 for _ in range(len(nums))]
        res = []
        for i in nums:
            total *= i
        for i in nums:
            res.append(total // i)
        
        
        return res