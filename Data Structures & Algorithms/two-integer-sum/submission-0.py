class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        index=0;
        for num in nums:  
            if num in hashMap:
                return [hashMap[num],index]
            complement = target-num
            hashMap[complement]=index
            index=index+1
            print(hashMap)
        return [-1,-1]