class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''.join(e for e in s if e.isalnum()).upper()
        j=len(a)-1
        i=0
        while i<j:
                if a[i]!=a[j]:
                    return False
                i+=1
                j-=1
        return True
        