class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        res = []
        
        def backtracking(index, curr_sum, lis):
            if curr_sum == target:
                res.append(lis[:])
                return


            #contraint
            if curr_sum > target or index >= len(nums):
                return
            
            lis.append(nums[index])
            backtracking(index, curr_sum + nums[index], lis)
            lis.pop()
            backtracking(index+1, curr_sum, lis)
        
        backtracking(0,0,[])
        return res