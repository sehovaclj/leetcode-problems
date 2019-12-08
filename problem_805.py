
"""

805. Split Array With Same Average
Hard

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.

Note:

    The length of A will be in the range [1, 30].
    A[i] will be in the range of [0, 10000].

"""


import bisect
from itertools import combinations

class Solution(object):
	def splitArraySameAverage(self, A):
		# first sort the array A
		A.sort()
		if len(A) == 1:
			return False # can't have two non-empty sets with only one element in A

		min_A = A[0] # get min
		max_A = A[-1] # get max

		if min_A == max_A: # if min of A is the same as the max of A, auto return true
			return True

		if len(A) == 2: # if length is 2 and the min is not max, auto return False
			if min_A != max_A:
				return False

		# if the array is all one number (min or max) except for one element, auto return false
		if (A.count(min_A) > len(A)-2) or (A.count(max_A) > len(A)-2):
			return False

		# obtain the average of A
		mu_A = sum(A) / len(A)

		# so I solved this problem using math/number theory, as opposed to data structures / programming practices.
		# I will try and explain it as best I can in this comment:
		#	See that, the average of array A, or 1/n Sum_i=1_to_n of A_i, is equal to the sum of 1/n Sum_i=1_to_n/2 (B_i + C_i).
		# However, it could also be the case that:
		#	1/n Sum_i=1_to_n (A_i) = b + 1/(n-1) Sum_i=1_to_n-1 (C_i), where b is just one element, and also the case that,	
		#	1/n Sum_i=1_to_n (A_i) = 1/2 Sum_i=1_to_2 (B_i) + 1/(n-2) Sum_i=1_to_n-2 (C_i) and also the case that,
		#	1/n Sum_i=1_to_n (A_i) = 1/3 Sum_i=1_to_3 (B_i) + 1/(n-3) Sum_i=1_to_n-3 (C_i) and this pattern continues for n until n = n/2 :: because if n = n/2 + 1, we can just interchange B and C and get terms we have already accounted for.
		# ALSO, it is important to note from the wording of the problem, that we do not need to actually find B and C, just return the boolean value of True or False.
		# Thus, we can think of C as "the remaining elements in A" and only need to find the elements in B that share the same average as the initial array A.
		# Let's look at an example. If A is an array of 10 elements, and has an average of 8.0, then all we need to do is find one element in A (8) that is equal to the average.
		# If we find the element (8), we auto return True -- since we found b, and we know (by the math above), that the remaining elements in A (or C), will share the same average (8).
		# If we don't find the element, we look for 2 numbers that average to 8. If we can't find 2 numbers, we try 3. If we can't find 3, we try 4. If we can't find 4 (4 elements in B, 6 elements in C), we try 5.
		# If we can't find 5 numbers in A that average to 8, then we auto return False, since trying 6 numbers would be equivalent to trying 4 numbers (6 elements in B, 4 elements in C == 2 lists sharing same average with one containing 4 and other 6).
		# In order to save time, we notice that if we multiply the average of A with the n, or number of elements in B we are trying to find, and this output isn't a whole number (integer), we move on to the next "multiplier" -- denote it q.
		# Hence, if q*mu is not a whole number (where integers can sum to), we check the next q.
		# If you are confused about my explanation, feel free to email me, in latex form or something it may be a lot easier to follow.

  
		# this is like the first loop of the loop below
		# hence, we are looking for one element in A that is equal to the average
		if mu_A % 1 == 0:
			index = bisect.bisect_left(A, int(mu_A))
			if A[index] == int(mu_A):
				return True

		# this if-else is so that q_list does not return an empty list if A is length 3.
		# I use the variable name q_list to store all "multipliers" q that when multiplied to the mean of A (mu_A) still produce whole numbers (or very very close -- hence use 1e-14, not 0).
		if (len(A)//2 + 1) == 2:
			q_list = [2]
		else:
			q_list = list(range(2, (len(A)//2)+1))

		results_bool = []

		for i in q_list:
			if (i*mu_A % 1 < 1e-14):
				results_bool.append((True, i))
			else:
				results_bool.append((False, 0))

		# if no q multiplies the mean into an integer, then automatically return False (bottom of script)
		for result in results_bool:
			if result[0] == True:
				num_numbers = result[1]
				sum_to = num_numbers*mu_A
				if (sum_to % 1) < 1e-14:
					sum_to = int(sum_to)
				# here, combinations takes the most time, the rest of the code. I could try and optimize the time complexity the most here.. but this is sort of like a seperate problem, and it's not too bad (see picture for speed comparison with other submissions).
				for combo in combinations(A, num_numbers):
					if sum(combo) == sum_to: # if sum of the combo is equivalent ot sum_to, auto return True -- we have found our B, hence remaining of A == C, thus can auto return True
						return True
		return False
		




