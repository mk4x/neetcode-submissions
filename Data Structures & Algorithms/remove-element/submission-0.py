class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        swapped = 0
        correct_from_right_until = n-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                swapped += 1
                while i < correct_from_right_until:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i += 1
        return n-swapped

