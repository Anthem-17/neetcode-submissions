from collections import defaultdict
d = defaultdict(list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list);
        str1 = strs.copy()
        for i in range(0,len(str1)):
            str1[i] = "".join(sorted(str1[i]))

        for j in range(0, len(str1)):
            groups[str1[j]].append(strs[j])

        return list(groups.values())

