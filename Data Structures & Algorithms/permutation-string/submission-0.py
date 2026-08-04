class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        currSub = []
        for r in range(len(s2)):
            currSub.append(s2[r])
            if ((r-l+1) == len(s1)):
                if(sorted(currSub) == sorted(s1)):
                    return True
                
                currSub.remove(s2[l])
                l+=1
            
        
        return False