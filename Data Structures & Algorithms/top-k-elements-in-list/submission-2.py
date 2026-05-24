class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        bucket = list(counter.items())

        upper = max(counter.values())
        lower = min(counter.values())

        counter = [[] for _ in range(upper - lower + 1)]


        for key, value in bucket:

            counter[value - lower].append(key)
        

        res = []

        for i in range(len(counter) -1, -1, -1):

            while counter[i] and len(res) < k:
                res.append(counter[i].pop())
            if len(res) == k:
                break
        
        return res




        