class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        postfix = [1] * len(nums) 
        result = []
        

        prev = 1
        for num in nums:
            prefix.append(prev) 
            prev = prev * num  


        post = 1
        j = len(nums) - 1
        while j >= 0:
            postfix[j] = post   
            post = post * nums[j] 
            j -= 1

        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])

        return result

        