# This solution is for the input num is sorted.
# This solution used two pointer , one searches from beginning, the other one from end.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return []

if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
    print solution.twoSum([0, 4, 3, 0], 0)
    print solution.twoSum([-3, 4, 3, 90], 0)
