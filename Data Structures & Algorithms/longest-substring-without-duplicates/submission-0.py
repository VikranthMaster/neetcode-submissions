class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxSub = 0
        currSub = set()
        for r in range(len(s)):
            while s[r] in currSub:
                currSub.remove(s[l])
                l+=1
            
            currSub.add(s[r])
            maxSub = max(maxSub, r-l+1)
        
        return maxSub
