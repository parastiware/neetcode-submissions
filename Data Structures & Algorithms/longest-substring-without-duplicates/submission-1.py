class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        maxSub=0
        left=0
        right=0
        charMap={}
        while right<len(s):
            if s[right] not in charMap:
                charMap[s[right]]=right
                maxSub= max(right-left+1,maxSub)
                right+=1
            else:
                del charMap[s[left]]
                left+=1
        return maxSub
