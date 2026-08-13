class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(i,lis):
            res.append(lis[:1])
            
            for x in range(len(nums)):
                if i > x and nums[i] == nums[i-1]:
                    continue
                lis.append(nums[x])
                backtracking(i+1, lis)
                lis.pop()
        
        backtracking(0,[])
        return res