class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        i=0
        for num in nums:
          if(num in hashMap):
            return[hashMap[num],i]
          hashMap[target-num]=i
          i+=1
        return[-1,-1]