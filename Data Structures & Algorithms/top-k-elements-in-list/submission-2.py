class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for x in nums:
            hashMap[x] = hashMap.get(x,0)+1
        
        l = sorted(hashMap.items(), key = lambda x:x[1], reverse=True)
        return [x for x,y in l[:k]]