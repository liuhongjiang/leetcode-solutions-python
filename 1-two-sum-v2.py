# This solution is implemented after I saw the leetcode handbook
# And it introduced a hash table to store the value already processed.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_num = {}
        for i in range(len(nums)):
            if old_num.get(target - nums[i]) is not None:
                return [old_num.get(target - nums[i]) + 1, i + 1]
            else:
                old_num[nums[i]] = i

if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
    print solution.twoSum([0, 4, 3, 0], 0)
    print solution.twoSum([-3, 4, 3, 90], 0)
