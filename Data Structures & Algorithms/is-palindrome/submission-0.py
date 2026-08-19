class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = "".join(char for char in s if char.isalnum())
        slis = list(s)
        #slis.

       

        slisr = slis.copy()

        slisr.reverse()
        

        print(slis)
        print(slisr)


        if slisr == slis:
            return True

        return False

        
        