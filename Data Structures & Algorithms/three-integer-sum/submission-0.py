class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            l = x + 1
            r = len(nums) -1
            while l < r:
                if nums[l] + nums[r] == -(nums[x]):
                    res.append([nums[x],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                if nums[l] + nums[r] > -(nums[x]):
                    r-=1
                elif nums[l] + nums[r] < -(nums[x]):
                    l+=1
    
        return res


