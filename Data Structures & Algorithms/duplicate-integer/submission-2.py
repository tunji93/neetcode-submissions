class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False

        counter = Counter(nums)




        return max(counter.values()) > 1
        