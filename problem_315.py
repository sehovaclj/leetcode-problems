
"""
315. Count of Smaller Numbers After Self
Hard

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

"""



import bisect
import collections
import time


class Solution(object):
	def countSmaller(self, nums):
		t0 = time.time()
		counts = [0]*len(nums)
		A = sorted(nums)
		idx_count = 0
		while idx_count < len(nums):
			left = nums[idx_count]
			len_is_num_smaller = bisect.bisect_left(A, left)
			counts[idx_count] = len_is_num_smaller
			A.pop(len_is_num_smaller)
			idx_count += 1
		print("Total time to compute: {}".format(time.time()-t0))
		return counts 	



