class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        H = []


        for key in counter.keys():

            heapq.heappush(H, (counter[key], key))

            if len(H) > k:
                heapq.heappop(H)
        

        return [x[1] for x in H]
        