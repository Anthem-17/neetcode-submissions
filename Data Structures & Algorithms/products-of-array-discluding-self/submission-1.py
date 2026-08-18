class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pehle = [1] * len(nums)
        baadme = [1] * len(nums)
        final = [1] * len(nums)
        for i in range(len(nums)-1):
            pehle[i+1] = pehle[i] * nums[i]

        for j in range(len(nums)-1, 0, -1):
            baadme[j-1] = baadme[j] * nums[j]

        for k in range(len(nums)):
            final[k] = pehle[k] * baadme[k]

        return final

