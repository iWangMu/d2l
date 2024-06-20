import numpy as np
import display

def f(x):
    return 3 * x ** 2 - 4 * x

x = np.arange(0, 3, 0.1)
print(x)
display.plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])


