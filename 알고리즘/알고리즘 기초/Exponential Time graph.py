import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.arange(1, 10)   # X-axis: n 값 (1부터 9까지)
y = 10**x               # O(10^n): 지수 시간 복잡도

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="O(10^n): Exponential Time Complexity", color="purple")

# Customize the graph
plt.title("Exponential Time Complexity (O(10^n))", fontsize=14)
plt.xlabel("Input Size (n)", fontsize=12)
plt.ylabel("Number of Steps", fontsize=12)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=10)

# Show the graph
plt.tight_layout()
plt.show()
