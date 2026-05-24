class Solution:

    def encode(self, strs: List[str]) -> str:

        coded = ""

        for i in range(len(strs)):
            curr = strs[i]
            n = len(curr)

            coded += str(n) + "#" + curr
        return coded

    def decode(self, s: str) -> List[str]:

        res = []

        n = len(s)

        count = 0
        

        r = 0

        while r < n:

            if s[r] == "#":
                r+=1
                word = ""
                
                while count > 0 and r <n:
                    word+=s[r]
                    count-=1
                    r+=1
                res.append(word)
                
            else:
                count = (count * 10) + int(s[r])
                r+=1
        
        return res




