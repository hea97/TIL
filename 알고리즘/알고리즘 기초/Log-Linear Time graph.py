import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(1, 30, 100)  # X-axis: 1 to 30
y = x * np.log2(x)           # O(n log n)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, color="purple", label="O(n log n)")

# Axis settings
plt.title("Linear-Logarithmic Time Complexity O(n log n)", fontsize=14)
plt.xlabel("Number of Customers", fontsize=12)
plt.ylabel("Number of Steps", fontsize=12)
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=10)

# Show
plt.tight_layout()
plt.show()
