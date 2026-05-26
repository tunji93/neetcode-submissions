class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()


        res = []

        def backtrack(i, curr, target):

            if target == 0:
                res.append(curr[:])
                return
            
            if target < 0 or i == len(nums):
                return 
            

            for j in range(i, len(nums)):

                if j == i or nums[j] != nums[j-1]:
                    curr.append(nums[j])
                    backtrack(j+1, curr, target - nums[j])
                    curr.pop()
        
        backtrack(0, [], target)
        return res


        