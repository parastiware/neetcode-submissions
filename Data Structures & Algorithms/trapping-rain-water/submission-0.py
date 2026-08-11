class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[0]*len(height)
        maxRight=[0]*len(height)
        currLeftMax=0
        currRightMax=0
        totalWater=0
        for i,item in enumerate(height):
            maxLeft[i] =currLeftMax
            rightIndex=len(height)-i-1
            maxRight[rightIndex]=currRightMax
            if item>currLeftMax:
                currLeftMax=item
            if height[rightIndex]>currRightMax:
                currRightMax=height[rightIndex]
        
        for i,itemMax in enumerate(maxLeft):
            currWaterTrap=0
            if itemMax<maxRight[i]:
                currWaterTrap= itemMax-height[i]
            else:
                currWaterTrap= maxRight[i]-height[i]
            if currWaterTrap>0:
                totalWater+=currWaterTrap
        
        return totalWater

        