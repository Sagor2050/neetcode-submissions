class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        for i in range(k):
            result.append(0)
        
        my_dict = {}

        for val in nums:

            if val in my_dict:
                my_dict[val] += 1

            else:
                my_dict[val] = 1


        sorted_keys = sorted(my_dict, key = my_dict.get, reverse = True)

        return sorted_keys[ : k]

        
