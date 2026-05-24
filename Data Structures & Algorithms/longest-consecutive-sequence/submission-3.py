class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        

        nums.sort()

        n = len(nums)

        res = 1
        count = 1



        for r in range(1, n):

            if nums[r] == nums[r-1]:
                continue

            if nums[r] == nums[r-1] + 1:
                count+=1
                
            else:
                res = max(res,count)
                count = 1
        
        return max(count, res)

        


            