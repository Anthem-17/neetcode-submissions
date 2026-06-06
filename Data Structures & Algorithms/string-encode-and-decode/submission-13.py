class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for k in strs:
            res += str(len(k)) + "#" + k

        return res

        

    def decode(self, s: str) -> List[str]:
        l1 = []

        total = len(s)
        i = 0
        while i < total:
            leng = ""
            while s[i] != "#":
                leng += str((s[i]))
                i += 1

            jump = i + 1 + int(leng) 
            b = i+1
            word = ""
            for j in range(b, jump):
                word += s[j]
            
            l1.append(word)
            i=jump

        return l1


            
