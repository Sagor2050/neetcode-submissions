class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        result = []

        for i, val in enumerate(nums):
            comp = target - val

            if val in seen:
                result.append(seen[val])
                result.append(i)
                return result
            
            seen[comp] = i

        return result 

            

            
        