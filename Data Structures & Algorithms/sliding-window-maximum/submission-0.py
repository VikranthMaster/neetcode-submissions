class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ansArr = []
        currArr = []
        for r in range(len(nums)):
            currArr.append(nums[r])
            if (r-l+1 == k):
                ansArr.append(max(currArr))
                currArr.remove(nums[l])
                l+=1
        
        return ansArr
