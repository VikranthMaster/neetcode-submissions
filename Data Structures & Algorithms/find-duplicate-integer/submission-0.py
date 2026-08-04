class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        someDict = {}
        for x in nums:
            someDict[x] = someDict.get(x,0)+ 1

        for x, v in someDict.items():
            if v > 1:
                return x