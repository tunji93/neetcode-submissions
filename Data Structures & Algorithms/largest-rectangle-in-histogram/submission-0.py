class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        res = 0
        n = len(heights)


        for i, height in enumerate(heights):

            idx = i


            while stack and height <= stack[-1][1]:

                idx, prev = stack.pop()
                

                res = max(res, (i-idx) * prev)
            
            stack.append((idx, height))
        
        
        

        while stack:

            idx, prev = stack.pop()
            res = max(res, (n-idx)*prev)
        return res

        