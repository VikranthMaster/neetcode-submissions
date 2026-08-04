class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        someHash = {}
        maxSub = 0

        while r < len(s):
            someHash[s[r]] = someHash.get(s[r], 0)+1
            winSize = r - l +1
            if(winSize - max(someHash.values()) > k):
                someHash[s[l]] -=1
                l+=1

            maxSub = max(maxSub, r-l+1)
            r+=1
        
        return maxSub
