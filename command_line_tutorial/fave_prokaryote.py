import matplotlib.pyplot as plt
import numpy as np

# Generate plotting values
t = np.linspace(0, 2*np.pi, 200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Initialise figure
fig, ax = plt.subplots(figsize=(9,9))

# define plot and text
ax.plot(x, y, color='red', lw=3)
ax.text(x=-3.5, y=0, s='$Myxococcus xanthus$')

plt.show()