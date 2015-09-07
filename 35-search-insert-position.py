# binary search
# and it doesn't require move the element of this array


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left if nums[left] > target else left + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.searchInsert([1, 3, 5, 6], 5)
    print solution.searchInsert([1, 3, 5, 6], 2)
    print solution.searchInsert([1, 3, 5, 6], 7)
    print solution.searchInsert([1, 3, 5, 6], 0)

