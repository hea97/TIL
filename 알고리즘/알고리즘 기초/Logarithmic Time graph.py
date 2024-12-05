import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성 (로그 시간 복잡도) # Logarithmic time complexity (log2(n))
x = np.linspace(1, 30, 500)  # x축: 고객 수 (1부터 30까지) # X-axis: Number of customers (from 1 to 30)
y = np.log2(x)                # 로그 시간 복잡도 (log2(n)) # Logarithmic time complexity (log2(n))

# 그래프 그리기 # Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="O(log n)", color="purple", linewidth=2)

# 그래프 꾸미기 # Customize the graph
plt.title("Logarithmic Time Complexity O(log n)", fontsize=14, fontweight='bold')  # Title
plt.xlabel("Number of Customers", fontsize=12)  # X-axis label
plt.ylabel("Number of Steps", fontsize=12)  # Y-axis label
plt.ylim(0, 30)  # Set y-axis limit to 30
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=10, loc='upper left', frameon=False)  # Move the legend to the top left and remove the box
plt.tight_layout()

# 그래프 출력 # Show the graph
plt.show()
