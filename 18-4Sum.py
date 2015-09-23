# This solution take 760 ms.


class Solution(object):
    def _twoSum(self, nums, target, n_sum, *current_list):
        if len(nums) <= 1:
            return
        if nums[0] + nums[1] > target:
            return
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                tmp = list(reversed(current_list))
                tmp.extend([nums[i], nums[j]])
                n_sum.append(tmp)
                while i < j:
                    if nums[i] == nums[i + 1]:
                        i += 1
                    elif nums[j] == nums[j - 1]:
                        j -= 1
                    else:
                        i += 1
                        break
        return

    def _NSum(self, nums, target, n_sum, n, *current_list):
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if n * nums[i] > target:
                break
            if n - 1 == 2:
                self._twoSum(nums[i + 1:], target - nums[i], n_sum, nums[i], *current_list)
            else:
                self._NSum(nums[i + 1:], target - nums[i], n_sum, n-1, nums[i], *current_list)
        return

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        four_sum = []
        current_list = []
        self._NSum(nums, target, four_sum, 4, *current_list)
        return four_sum
