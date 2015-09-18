class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_water = min(height[i], height[j]) * (j - i)

        while i < j:
            if height[i] < height[j]:
                k = i + 1
                while height[i] > height[k] and k < j:
                    k += 1
                i = k
            else:
                k = j - 1
                while height[j] > height[k] and k > i:
                    k -= 1
                j = k
            water = min(height[i], height[j]) * (j - i)
            max_water = max_water if max_water >= water else water

        return max_water

