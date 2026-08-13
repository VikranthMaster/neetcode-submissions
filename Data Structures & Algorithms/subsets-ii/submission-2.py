class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtracking(i,lis):
            res.append(lis[:])
            
            for x in range(i,len(nums)):
                if x > i and nums[x] == nums[x-1]:
                    continue
                lis.append(nums[x])
                backtracking(x+1, lis)
                lis.pop()
        
        backtracking(0,[])
        return res