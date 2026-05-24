class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)

        if m !=n:
            return False
        
        counterS = [0] * 26
        counterT = [0] * 26

        for i in range(n):

            idx = ord(s[i]) - ord("a")
            counterS[idx]+=1
            idx = ord(t[i]) - ord("a")
            counterT[idx] += 1
        
        return counterS == counterT
        