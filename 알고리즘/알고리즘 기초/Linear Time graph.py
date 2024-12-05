import matplotlib.pyplot as plt
import numpy as np

# Generate data for linear time complexity (O(n))
x = np.linspace(1, 30, 30)  # X-axis: number of customers (1 to 30)
y = x                        # Linear time complexity: O(n), where y = n

# Create graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="O(n): Linear Time Complexity", color="green")

# Customize the graph
plt.title("Linear Time Complexity (O(n))", fontsize=14)
plt.xlabel("Number of Customers (X-axis)", fontsize=12)  # X축 레이블
plt.ylabel("Number of Steps (Y-axis)", fontsize=12)      # Y축 레이블
plt.xlim(0, 30)  # Set x-axis limit to 30  # X축 최대값을 30으로 설정
plt.ylim(0, 30)  # Set y-axis limit to 30  # Y축 최대값을 30으로 설정
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)  # 그리드 추가
plt.legend(fontsize=10)  # 범례 추가
plt.tight_layout()

# Show the graph
plt.show()
