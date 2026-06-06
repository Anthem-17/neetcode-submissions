class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        countt = [0]*26
        for i in range(0, len(s)):
            counts[ord(s[i])-97]+= 1

        for j in range(0, len(t)):
            countt[ord(t[j])-97]+= 1

        if counts == countt:
            return True
            exit

        return False
            
