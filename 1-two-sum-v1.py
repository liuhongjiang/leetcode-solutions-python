# The original version implemented by my self.
# This solution sort the list first, then used a o(n) method.

import copy


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_nums = copy.deepcopy(nums)
        sort_nums.sort()
        i = 0
        j = len(sort_nums) - 1
        while i < j:
            if sort_nums[i] + sort_nums[j] == target:
                break
            elif sort_nums[i] + sort_nums[j] > target:
                j -= 1
            else:
                i += 1
        if i >= j:
            return []
        index1 = None
        index2 = None
        for k in range(len(nums)):
            if index1 is None and nums[k] == sort_nums[i]:
                index1 = k
            elif index2 is None and nums[k] == sort_nums[j]:
                index2 = k
        answer = [index1 + 1, index2 + 1]
        answer.sort()
        return answer

if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
    print solution.twoSum([0, 4, 3, 0], 0)
    print solution.twoSum([-3, 4, 3, 90], 0)
