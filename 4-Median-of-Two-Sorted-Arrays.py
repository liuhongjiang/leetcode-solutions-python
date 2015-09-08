# using the though of find kth items of two arrays
# before that I used the two pointer, start at the middle of two array, 
# then based on the value of the pointer to move the pointer to the middle of the half part..
# But this method is very hard to compute the median if the total length of two array are even.
# The Kth solution is much better.


def find_kth_item(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    if len(nums1) == 0:
        return nums2[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])
    k_in_nums1 = min(k / 2, len(nums1))
    k_in_nums2 = k - k_in_nums1
    if (nums1[k_in_nums1 - 1]) == (nums2[k_in_nums2 - 1]):
        return nums1[k_in_nums1 - 1]
    elif (nums1[k_in_nums1 - 1]) < (nums2[k_in_nums2 - 1]):
        return find_kth_item(nums1[k_in_nums1:], nums2, k - k_in_nums1)
    else:
        return find_kth_item(nums1, nums2[k_in_nums2:], k - k_in_nums2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return find_kth_item(nums1, nums2, (total + 1) / 2)
        else:
            return (find_kth_item(nums1, nums2, total / 2) + find_kth_item(nums1, nums2, total / 2 + 1)) / 2.0


if __name__ == "__main__":
    solution = Solution()
    print "1 Answer 5.5: ", solution.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    print "2 Answer 5: ", solution.findMedianSortedArrays([1, 2, 4], [3, 5, 6, 7, 8, 9])
    print "3 Answer 5: ", solution.findMedianSortedArrays([1, 2, 5], [3, 4, 6, 7, 8, 9])
    print "4 Answer 10: ", solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 18, 19],
                                                           [9, 10, 11, 12, 13, 14, 15, 16, 17])
    print "5 Answer 10: ", solution.findMedianSortedArrays(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [10])
    print "6 Answer 10: ", solution.findMedianSortedArrays([], [10])
    print "7 Answer 2.5: ", solution.findMedianSortedArrays([], [2, 3])
    print "8 Answer 3: ", solution.findMedianSortedArrays([1, 5], [2, 3, 4])
    print "9 Answer 5: ", solution.findMedianSortedArrays([1, 5], [2, 3, 4, 6, 7, 8, 9])
    print "10 Answer 1.5: ", solution.findMedianSortedArrays([1, 2], [1, 2])
    print "11 Answer 2.5: ", solution.findMedianSortedArrays([1], [2, 3, 4])
