class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for val in nums:
            my_dict[val] = my_dict.get(val, 0) + 1

        sorted_keys = sorted(my_dict, key = my_dict.get, reverse = True)

        return sorted_keys[ : k]

        
