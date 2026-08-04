class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash1 = {}

        for x in t:
            hash1[x] = hash1.get(x,0) + 1
        
        l = 0
        hash2 = {}
        res = ""
        smallest = float("inf")

        for r in range(len(s)):
            hash2[s[r]] = hash2.get(s[r],0) + 1
            while all(hash2.get(c,0) >= hash1[c] for c in hash1):
                if r-l + 1 < smallest:
                    smallest = r-l+1
                    res = s[l:r+1]

                hash2[s[l]] -= 1
                if hash2[s[l]] == 0:
                    del hash2[s[l]]
                
                l+=1
            
        
        return res
        

                