from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict(int)
        j = 0
        
        for i in nums:
            if(target-i) in x:
                return [x[target-i], j]
            x[i] = j
            j += 1

       

        

