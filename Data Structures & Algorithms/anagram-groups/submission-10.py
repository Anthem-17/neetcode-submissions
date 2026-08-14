from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        strsdupe = list()
        for str1 in strs:
            strsdupe.append("".join(sorted(str1)))

        x = len(strsdupe)

        for i in range(x):
            d[strsdupe[i]].append(strs[i])

        result = [["a"] for _ in range(len(strs))]

        return list(d.values())