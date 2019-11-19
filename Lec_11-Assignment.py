import numpy as np
import matplotlib.pyplot as plt

nums_1 = np.array([1, 2, 3, 4, 5])

nums_2 = np.array([9, 8, 7, 6, 5])

# problem 1
nums_3 = np.array(nums_1 + nums_2)

# problem 2
nums_4 = nums_2 * 4

# problem 3
np.dot(nums_3, nums_4)

# problem 4

nums_5 = np.array([np.mean(nums_1), np.std(nums_1), np.var(nums_1)])




range_of_nums = np.arange(0, 100)

# problem 5
nums_6 = range_of_nums[::5]

# problem 6

# get every 3 elements in a reversed range_of_nums
nums_reverse = range_of_nums[::-1]
nums_7 = nums_reverse[::3]

# problem 7

plt.plot(np.random.random((100, 100)))
plt.savefig("figure_1.png")

# problem 8

nums_8 = np.linspace(0, 100, 25)
nums_9 = np.array([np.linspace(0, 5, 50), np.linspace(5, 10, 50)])

nums_10 = np.linspace(0, 10, 100)
nums_10_times_2 = nums_10 * 2
# do you mean 2 rows or multiply by 2?

nums_11 = nums_8[1:6]
nums_12 = nums_9[1]
nums_13 = nums_12[1:6]
plt.plot(nums_11, nums_13)
plt.savefig("figure_2.png")

# problem 9


nums_rand_a = np.random.random((4, 4))
nums_rand_b = np.random.random((4, 4))
nums_rand_sum = nums_rand_a + nums_rand_b

