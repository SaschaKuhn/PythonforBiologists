import numpy as np
import matplotlib.pyplot as plt

# Generate plotting values
t = np.linspace(0, 2*np.pi, 200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots()
ax.plot(x, y, color='red', lw=3)
ax.text(x=-3.5, y=0, s='Plinius Cursus')

plt.show()