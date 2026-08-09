class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        left=0;
        right=len(heights)-1
        while left<right:
            area=0
            if heights[left]>heights[right]:
                area= heights[right]*(right-left)
                right-=1
            else:
                area= heights[left]*(right-left)
                left+=1
            maxArea=max(maxArea,area)
        return maxArea


        