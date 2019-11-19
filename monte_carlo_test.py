import sys
import monte_carlo

# we run the program with python test.py 1
print(sys.argv[1])

#output
1

# so now we can do
def func(x):
  return 1 + np.sin(x)

# have the steps be dependent on the input
area, x, y, check = monte_carlo.integrate(0, 1, func, int(sys.argv[1]))
