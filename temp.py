from Genration_Of_Images import Generate_Images , Show_Image
from func.SpeakOffline import Speak
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def equation(x):
    return 251.5 * x + 2

# Generate x values
x_values = np.linspace(-10, 10, 100)

# Calculate corresponding y values
y_values = equation(x_values)

# Plot the graph
plt.plot(x_values, y_values, label='2 = 251.5 * x + 2')
plt.title('Graph of 2 = 251.5 * x + 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()