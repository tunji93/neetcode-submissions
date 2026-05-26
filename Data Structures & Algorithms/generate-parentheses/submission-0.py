class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def backtrack(open, close, curr):

            if open == n and close == n:
                res.append("".join(curr))
                return
            if open> n or  close > n:
                return 
            
            if open < n:
                curr.append("(")
                backtrack(open+1,close,curr)
                curr.pop() 
            
            if open > close:
                curr.append(")")
                backtrack(open,close+1,curr)
                curr.pop() 

                      
            
        
        backtrack(0,0,[])

        return res



        