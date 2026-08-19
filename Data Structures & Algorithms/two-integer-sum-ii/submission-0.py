from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #d1 = defaultdict()
        d2 = defaultdict()
        for i in range(len(numbers)):
            #d1[i] = numbers[i]
            d2[numbers[i]] = i

        for i in range(len(numbers)):
            if target - numbers[i] in d2:
                if d2[target-numbers[i]] < i:
                    return[d2[target-numbers[i]]+1, i+1]

                else:
                    return[i+1, d2[target-numbers[i]]+1]


        