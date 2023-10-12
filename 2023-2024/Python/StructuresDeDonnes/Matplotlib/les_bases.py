"""
Les bases de numpy et matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

"""x = np.array([1, 1.5, 2, 2.5])
y = np.array([2.0, 3.0, 4.0, 5.0])
plt.plot(x, y)
plt.show()
"""

# Courbe avec fonction mathématique:

x = np.linspace(0, 20, 10)
y = 2*x**2+3
"""plt.plot(x, y)
plt.show()"""

# Option de couleur:
plt.plot(x, y, "r")
plt.show()