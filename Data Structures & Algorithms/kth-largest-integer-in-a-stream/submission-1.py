class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.H = nums
        heapq.heapify(self.H)
        self.k = k
        

    def add(self, val: int) -> int:

        heapq.heappush(self.H, val)

        while len(self.H) > self.k:
            heapq.heappop(self.H)
        
        return self.H[0]
        
