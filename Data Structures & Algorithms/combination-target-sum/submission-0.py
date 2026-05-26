class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, curr, total):

            if total == 0:

                res.append(curr[:])
                return
            
            if total < 0:
                return
            if i == len(nums):
                return
            

            curr.append(nums[i])
            backtrack(i, curr, total-nums[i])
            curr.pop()
            backtrack(i+1, curr, total)
        

        backtrack(0, [], target)

        return res
        




        