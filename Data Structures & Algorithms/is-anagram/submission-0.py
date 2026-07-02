class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        agram1= {}
        agram2= {}
        if len(s) != len(t):
            return False
        else:
            for char in s:
                agram1[char]= agram1.get(char,0)+1
            for char in t:
                agram2[char]= agram2.get(char,0)+1
            return agram1 == agram2

