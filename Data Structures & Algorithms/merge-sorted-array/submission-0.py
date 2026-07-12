from bisect import bisect_left
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        def get_pos(arr, l, r, val):
            while l < r:
                mid = (l+r)//2
                if arr[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        for i in range(n):
            del nums1[-1]
        for i in nums2:
            pos = get_pos(nums1, 0, len(nums1), i)
            nums1.insert(pos, i)