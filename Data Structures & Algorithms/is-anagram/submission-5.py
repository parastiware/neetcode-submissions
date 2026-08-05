class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
          return False
        s=s.upper()
        t=t.upper()
        feq1=[]
        feq2=[]
        for i in range(26):
            feq1.append(0)
            feq2.append(0)
        for char in s:
           print(ord(char)-65)
           feq1[ord(char)-65]+=1
        for char in t:
           print(ord(char)-65)
           feq2[ord(char)-65]+=1

        for i in range(26):
           if feq1[i]!=feq2[i]:
                return False
        return True

        