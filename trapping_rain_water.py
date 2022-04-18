class Solution(object):
    def trap(self, height):
        low = 0
        high = len(height) - 1
        res = 0
        low_max = 0
        high_max = 0

        while(low <= high):
            if (height[low] < height[high]):
                if (height[low] > low_max):
                    low_max = height[low]
                else:
                    res += low_max - height[low]
                low += 1
            else:
                if (height[high] > high_max):
                    high_max = height[high]
                else:
                    res += high_max - height[high]
                high -= 1
        return res
