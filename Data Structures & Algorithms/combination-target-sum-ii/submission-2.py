class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtracking(i, lis, curr):
            if curr == target:
                res.append(lis[:])
                return

            if curr > target:
                return
            
            for x in range(i, len(candidates)):
                if x > i and candidates[x] == candidates[x-1]:
                    continue
                
                lis.append(candidates[x])

                backtracking(x+1, lis, curr + candidates[x])
                lis.pop()
        
        backtracking(0,[],0)
        return res
