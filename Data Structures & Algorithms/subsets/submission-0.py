class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def something(i,lis):
            if i == len(nums):
                res.append(lis[:])
                return
            
            lis.append(nums[i])
            something(i+1, lis)
            lis.pop()

            something(i+1, lis)
        
        something(0,[])
        return res
