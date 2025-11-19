class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            h = min(height[l], height[r])
            width = (r - l)
            curr_area = h * width
            max_area = max(max_area, curr_area)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1

        return max_area
