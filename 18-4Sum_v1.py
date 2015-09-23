class Solution(object):
    def _compute2Sum(self, nums):
        two_sum_dict = {}
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                two_sum_list = two_sum_dict.get(nums[i] + nums[j])
                if two_sum_list is not None:
                    two_sum_list.append([nums[i], nums[j]])
                else:
                    two_sum_dict[nums[i] + nums[j]] = [[nums[i], nums[j]]]
        return two_sum_dict

    def _count_num(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        return num_count

    def _enough_numbers(self, num_count, tmp):
        for num in tmp:
            if num_count[num] < tmp.count(num):
                return False
        return True

    def _combine_two_sum(self, four_sum, num_count, list1, list2):
        for item1 in list1:
            for item2 in list2:
                tmp = list(item1)
                tmp.extend(item2)
                tmp = sorted(tmp)
                if self._enough_numbers(num_count, tmp):
                    four_sum.append(tmp)
        return

    def _remove_duplicate(self, four_sum):
        sum_dict = {"%d,%d,%d,%d" % tuple(one_sum): one_sum for one_sum in four_sum}
        return [v for k, v in sum_dict.iteritems()]

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        num_count = self._count_num(nums)
        two_sum_dict = self._compute2Sum(nums)

        four_sum = []
        for key, value in two_sum_dict.iteritems():
            if two_sum_dict.get(target - key):
                self._combine_two_sum(four_sum, num_count, value, two_sum_dict[target - key])
                two_sum_dict[key] = []
                two_sum_dict[target - key] = []
        return self._remove_duplicate(four_sum)
