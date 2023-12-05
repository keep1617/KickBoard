import time
import random
import numpy as np

# 2D 배열 초기화
two_d_array = [[] for _ in range(5)]  # 5개의 빈 리스트를 갖는 2D 배열

# 90초 동안 1초에 1번씩 랜덤 리스트를 생성하여 2D 배열에 추가
for second in range(1, 91):
    # 5개의 요소를 가진 랜덤 리스트 생성
    element_list = [random.randint(1, 100) for _ in range(5)]
    
    # 각 리스트에 요소 추가
    for index, element in enumerate(element_list):
        two_d_array[index].append(element)
    
    # 1초 대기
    time.sleep(1)

# 결과 출력
for i, col in enumerate(two_d_array):
    print(f"Column {i+1}: {col}")
    col_np = np.array(col)
    col_mean = np.mean(col_np)
    col_std = np.std(col_np)
    print(f"  Mean: {col_mean:.2f}")
    print(f"  Standard Deviation: {col_std:.2f}")
    print()