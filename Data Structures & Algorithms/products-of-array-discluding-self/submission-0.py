class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*len(nums)
        right = [0]*len(nums)
        output = [0]*len(nums)

        l = 1
        r = 1

        left[0] = 1
        right[n-1] = 1

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]

        for j in range(n-2, -1, -1):
            right[j] = right[j+1]*nums[j+1]

        for k in range(0, n):
            output[k] = left[k] * right[k]

        return output



        


        
        