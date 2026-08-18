class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for ele in strs:
            encoded_str += ele +  "~"

        print(encoded_str)
        return encoded_str
        
        

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        j = 0
        while j < len(s):
            ind = s.find("~")
            decoded_str.append("".join(s[:ind]))
            i += 1
            s = s[ind+1:]

        return decoded_str


       