class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = []
        nums.sort()

        def backtrack(i, curr):

            res.append(curr[:])
            

            for j in range(i, len(nums)):

                if j == i or nums[j] != nums[j-1]:
                    curr.append(nums[j])
                    backtrack(j+1, curr)
                    curr.pop()
        
        backtrack(0, [])

        return res
        