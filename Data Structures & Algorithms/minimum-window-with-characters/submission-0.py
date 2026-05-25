class Solution:
    def minWindow(self, s: str, t: str) -> str:

        counterT = Counter(t)
        counterS = {}
        

        left = 0

        res = ""
        minWindow = float("inf")

        formed = 0

        for right in range(len(s)):

            ch = s[right]
            counterS[ch] = counterS.get(ch, 0) + 1

            if counterS[ch] == counterT.get(ch, float("inf")):
                formed +=1
            
            while formed == len(counterT):

                if right - left + 1 < minWindow:
                    res = s[left:right+1]
                    minWindow = right-left+1

                char = s[left]
                
                if char in counterT:
                    counterS[char] -=1
                    if counterS[char] < counterT[char]:
                        formed-=1
                left+=1
        
        return res

