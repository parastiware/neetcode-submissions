import re
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!= len(t)):
            return False;
        for character in s:
            if character not in t:
                return False;
            t=re.sub(character, "", t, 1)
            print(s)
            print(t)
        return True;
        