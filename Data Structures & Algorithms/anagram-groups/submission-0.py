class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = set()

        def check(t,s):

            if len(t) != len(s):
                return False
            
            counterT = [0] * 26
            counterS = [0] * 26

            for i in range(len(s)):

                idx = ord(s[i]) - ord("a")
                counterS[idx] += 1
                idx = ord(t[i]) - ord("a")
                counterT[idx] += 1
            
            return counterS == counterT
        
        res = []
        

        n = len(strs)

        for i in range(n):
            curr = strs[i]
            if curr in seen:
                continue
            temp = [curr]

            for j in range(i+1, n):
                if check(curr, strs[j]):
                    seen.add(strs[j])
                    temp.append(strs[j])
            seen.add(curr)
            res.append(temp)
        return res
        