# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i=1
        r=n
        ans=0
        while i<=r:
            m=(i+r)//2
            if isBadVersion(m)==False:
                i=m+1
            else:
                ans=m
                r=m-1
        return ans
        
        
 """
 Runtime: 51 ms, faster than 36.81% of Python3 online submissions for First Bad Version.
Memory Usage: 13.9 MB, less than 61.81% of Python3 online submissions for First Bad Version.
