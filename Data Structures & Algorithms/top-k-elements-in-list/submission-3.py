from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)

       bucket = [[] for _ in range(len(nums)+1)]

       for num,freq in count.items():
        bucket[freq].append(num)
    
       res = list()
       y = 0
    
       for i in range(len(bucket)-1, -1, -1):
        if bucket[i] != []:
            j = 0
            while j < len(bucket[i]):
                res.append(bucket[i][j])
                j += 1

       return res[:k]


       
       

        
