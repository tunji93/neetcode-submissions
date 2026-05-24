class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        seen = set(nums)
        res = 0

        for val in seen:

            if val - 1 in seen:
                continue

            curr = val
            
            count = 0

            while curr in seen:
                count +=1
                curr = curr + 1
            
            res = max(res, count)
        
        return res
            