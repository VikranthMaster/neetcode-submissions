class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            minHeight = heights[l] if heights[l] < heights[r] else heights[r]
            currArea = minHeight * (r-l)
            maxArea = max(currArea, maxArea)
            if minHeight == heights[l]:
                l+=1
            if minHeight == heights[r]:
                r-=1
        
        return maxArea