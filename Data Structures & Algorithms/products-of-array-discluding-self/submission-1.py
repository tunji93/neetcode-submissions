class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        

        left = [1] * n
        product = 1

        for i in range(1, n):

            left[i] = left[i-1] * nums[i-1]
        
        for i in range(n-1, -1, -1):

            left[i] = left[i] * product
            product = nums[i] * product
        

        
        
        return left