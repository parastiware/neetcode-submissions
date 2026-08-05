class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1;
        zeroCount=0;
        for num in nums:
            if(num!=0):
                product*=num;
            else:
                zeroCount+=1;


        if zeroCount==0:
              for i in range(len(nums)):
                nums[i]=int(product/nums[i]);

        elif zeroCount>1:
            for i in range(len(nums)):
                 nums[i]=0;
        elif zeroCount==1:
            for i in range(len(nums)):
                if(nums[i]!=0):
                    nums[i]=0;
                else:
                    nums[i]=product;
        return nums




