import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(1, 30, 30)  # X-axis: Number of elements (1 to 30)
y = 2 * x**2                # O(n^2) time complexity

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="O(n^2): Quadratic Time Complexity", color="purple")

# Customize the graph
plt.title("Quadratic Time Complexity (O(n^2))", fontsize=14)
plt.xlabel("Number of Elements (n)", fontsize=12)
plt.ylabel("Number of Steps", fontsize=12)
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=10)

# Show the graph
plt.tight_layout()
plt.show()
