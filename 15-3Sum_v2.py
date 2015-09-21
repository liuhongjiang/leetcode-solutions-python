class Solution(object):
    def _twoSum(self, nums, target, three_sum_dict):
        cache = {}
        for num in nums:
            if cache.get(target - num):
                tmp = sorted([target - num, num, -target])
                three_sum_dict["%d,%d,%d" % tuple(tmp)] = tmp
            else:
                cache[num] = 1
        return

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        three_sum_dict = {}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            self._twoSum(nums[i + 1:], -nums[i], three_sum_dict)

        three_list = [v for k, v in three_sum_dict.iteritems()]
        return three_list
