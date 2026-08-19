class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        i = 1
        j = 0

        prednahi = []
        

        for num in snums:
            if num-1 not in snums:
                prednahi.append(num)

        for num in prednahi:
            seed = num
            i = 1
            while(seed+1 in snums):
                i += 1
                seed += 1
            if i > j:
                j = i

        return j

        




      
        