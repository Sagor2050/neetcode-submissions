class Solution:
    def cal_area(self, left, right, l_val, r_val):
        width = right - left
        height = min(l_val, r_val)

        return width * height

    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maximum = -1

        while left < right:
            result = self.cal_area(left, right, heights[left], heights[right])

            if result > maximum:
                maximum = result
            
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1

        return maximum



    
        