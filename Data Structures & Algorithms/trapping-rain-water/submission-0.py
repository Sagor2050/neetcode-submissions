class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        start = 0
        end = len(height) -1

        max_left = []
        max_right = []


        for i in range(len(height)):
            max_right.append(0)

        maximum = 0

        for i, val in enumerate(height):        

            max_left.append(maximum)

            if height[i] > maximum:
                maximum = height[i]


        
        large_right = 0
        right = len(height) - 1

        while right != 0:
            max_right[right] = large_right

            if height[right] > large_right:
                large_right = height[right]

            right -= 1

        

        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]

            if water > 0:
                total_water += water

            
        return total_water

        


