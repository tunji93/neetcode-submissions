class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = []

        queue = deque()

        for r in range(len(nums)):
            curr = nums[r]

            while queue and nums[queue[-1]] < curr:
                queue.pop()
            
            while queue and r-queue[0] + 1 > k:
                queue.popleft()
            
            queue.append(r)

            if r >= k-1:

                res.append(nums[queue[0]])
        
        return res