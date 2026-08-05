import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap={};
        for num in nums:
            if num in countMap:
                countMap[num]= countMap[num]+1
            else:
                 countMap[num]=1

        output=[]
        maxValue=countMap[nums[0]]
        maxIndex=nums[0]
        for i in range(k):
             maxKey = max(countMap.items(), key=operator.itemgetter(1))[0]
             output.append(maxKey)
             countMap.pop(maxKey)
    
                 
        return output;
            
                 
                



        


        