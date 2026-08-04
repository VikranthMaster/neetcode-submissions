from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        someMap = defaultdict(list)

        for x,y  in enumerate(strs):
            y = sorted(y)
            y = "".join(y)
            someMap[y].append(x)
    
        l = []
        for x in someMap.values():
            l.append([strs[y] for y in x])
        
        return l
        
            