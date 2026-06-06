from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in range(0, len(nums)):
            d[nums[i]] += 1

        d1 = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))

        l = list(d1)[:k]
        

        return l;
        