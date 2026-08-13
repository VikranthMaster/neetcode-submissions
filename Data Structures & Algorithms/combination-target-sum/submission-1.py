class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        res = []
        
        def backtracking(index, curr_sum, lis):
            if curr_sum == target:
                res.append(lis[:])
                return


            #contraint
            if curr_sum > target:
                return
            
            for i in range(index, len(nums)):
                lis.append(nums[i])
                backtracking(i, curr_sum + nums[i], lis)
                lis.pop()
        
        backtracking(0,0,[])
        return res