class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            d[nums[i]] = i

        for j in range(0, len(nums)):
            if (target-nums[j]) in d:
                if d[target-nums[j]] < j and d[target - nums[j]] != j:
                    return [d[target-nums[j]],j]

                if d[target-nums[j]] > j and d[target - nums[j]] != j:
                    return[j,d[target-nums[j]]]


