import re
from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for string in strs:
            added = False
            for data in output:
                if self.isAnagram(data[0], string):  # Check if it's an anagram
                    data.append(string)
                    added = True
                    break
            if not added:  # If no anagram group is found, add a new group
                output.append([string])
        return output

    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        for char in a:
            if char in b:
                b = re.sub(char, "", b, 1)  # Remove matched character once
            else:
                return False
        return True
