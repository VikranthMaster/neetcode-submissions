class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(lis):
            if len(lis) == len(nums):
                res.append(lis[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in lis:
                    continue
                lis.append(nums[i])
                backtracking(lis)

                lis.pop()
                
        backtracking([])
        return res
        
