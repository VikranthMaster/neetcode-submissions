class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def backtrack(i,lis):
            if i == len(s):
                res.append(lis[:])
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    lis.append(substring)
                    backtrack(j+1, lis)
                    lis.pop()
        
        backtrack(0, [])
        return res