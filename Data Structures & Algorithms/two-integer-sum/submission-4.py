class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        someMap = {}

        for x,y in enumerate(nums):
            diff = target-y
            if diff in someMap:
                return [someMap[diff],x]
            
            someMap[y] = x
        