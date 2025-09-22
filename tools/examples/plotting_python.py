"""
Minimal Working Example: Plotting in Python
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 4, 1]})

plt.plot(data['x'], data['y'], marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Plot')
plt.show()
