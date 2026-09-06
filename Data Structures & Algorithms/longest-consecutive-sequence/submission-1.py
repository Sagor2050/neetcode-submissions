class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maximum = 0

        for val in seen:

            if (val -1) not in seen:
                total = 1

                while (val +1) in seen:
                    total += 1
                    val += 1

                if total > maximum:
                    maximum = total

        return maximum

            

