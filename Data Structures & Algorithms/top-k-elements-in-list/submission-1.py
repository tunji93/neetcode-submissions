class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        bucket = list(counter.items())

        n = len(bucket)
        k = n-k

        def quickSelect(left, right):

            ptr = left
            el = bucket[right][1]
            
            for r in range(left,right):

                if bucket[r][1] <= el:
                    bucket[r], bucket[ptr] = bucket[ptr], bucket[r]
                    ptr+=1
            
            bucket[ptr], bucket[right] = bucket[right], bucket[ptr]

            if ptr == k:
                return ptr
            
            if ptr > k:
                return quickSelect(left, ptr - 1)
            return quickSelect(ptr+1, right)
        
        ptr = quickSelect(0,n-1)

        return [x[0] for x in bucket[ptr:]]