class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        left = [0] * n

        right = [0] * n

        res = 0

        for i in range(1, n):

            left[i] = max(height[i-1], left[i-1])

        for i in range(n-2, -1, -1):

            right[i] = max(height[i+1], right[i+1])
        

        for i in range(n):

            volume = min(right[i], left[i]) - height[i]

            res += max(0, volume)
        
        return res
        


        