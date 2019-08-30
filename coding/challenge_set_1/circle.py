# Solution for Problem 1
import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)
from matplotlib.patches import Circle

# Creating the figure
plt.figure(figsize=(10,10))
plt.axes()
# Asking for a radius from the user
radius = float(input("Please type in a radius for the circle: "))

# Creating the circle object
circ = Circle((0,0), radius=radius, fc='g')

# Adding the circle as a patch to the figure
plt.gca().add_patch(circ)

# Scaling the axes
plt.axis("scaled")

# Finishing the plot
plt.show()
