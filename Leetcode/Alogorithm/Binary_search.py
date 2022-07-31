class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)-1
        i=0
        while i <=r:
            m=(r+i)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                i=m+1
            elif nums[m]>target:
                r=m-1
                
        return (-1)
        
        
        
"""
Runtime: 358 ms, faster than 55.06% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 22.77% of Python3 online submissions for Binary Search.
"""
