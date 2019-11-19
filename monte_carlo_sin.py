import numpy as np
import monte_carlo

def sine(x):
    return np.sin(x)


area, x, y, check = monte_carlo.integrate(0, 6, sine, 100000)
print(area*4)

monte_carlo.plot_integration(x, y, check, sine, "01.png")