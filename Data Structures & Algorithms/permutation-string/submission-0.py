class Solution:
    def checkInclusion(self, s: str, t: str) -> bool:
        
        counterS = Counter(s)
        counterT = {}

        left = 0

        for right in range(len(t)):

            if t[right] not in counterS:
                counterT = {}
            else:

                counterT[t[right]] = counterT.get(t[right], 0) + 1

                if counterT[t[right]] > counterS[t[right]]:

                    while counterT[t[right]] > counterS[t[right]]:

                        ch = t[left]
                        if ch in counterT:
                            counterT[ch] -=1
                        left+=1
            
            if counterT == counterS:
                return True
        
        return False