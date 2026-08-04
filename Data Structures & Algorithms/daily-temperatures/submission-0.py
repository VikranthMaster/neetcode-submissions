class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair [temp, index]

        for x,y in enumerate(temperatures):
            while stack and y > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (x - stackInd)
            
            stack.append([y,x])
        
        return res

