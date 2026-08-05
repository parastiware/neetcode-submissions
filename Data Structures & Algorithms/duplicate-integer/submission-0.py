class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable={};
        for num in nums:
            if num in hashTable:
                hashTable[num] =  hashTable[num]+1;
            else:
                hashTable[num] =  1
            if hashTable[num]>1:
                return True
            
        return False
