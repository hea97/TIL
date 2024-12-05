import matplotlib.pyplot as plt
import numpy as np

# Generate data
# 데이터 생성
x = np.linspace(0, 10000, 100)  # X-axis: number of customers
                                # X축: 고객 수
y = np.ones_like(x)             # Constant time complexity: O(1)
                                # 상수 시간 복잡도: O(1)

# Create graph
# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="O(1): Constant Time Complexity", color="blue")

# Customize the graph
# 그래프 꾸미기
plt.title("Constant Time Complexity (O(1))", fontsize=14)
plt.xlabel("Number of Customers (X-axis)", fontsize=12)  # X축 레이블
plt.ylabel("Number of Steps (Y-axis)", fontsize=12)      # Y축 레이블
plt.axhline(y=1, color='gray', linestyle='--', linewidth=0.8)  # y=1 기준선 추가
plt.xlim(0, 30)  # Set x-axis limit to 30  # X축 최대값을 30으로 설정
plt.ylim(0, 30)  # Set y-axis limit to 30  # Y축 최대값을 30으로 설정
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)  # 그리드 추가
plt.legend(fontsize=10)  # 범례 추가
plt.tight_layout()

# Show the graph
# 그래프 출력
plt.show()