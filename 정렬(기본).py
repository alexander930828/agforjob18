array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스

    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j  # 가장 작은 원소의 인덱스가 앞으로 오게하는 방법 /
            # for문은 계속해서 업데이트를 하고 주어진 범위내의 모든 수를 다 돌아야만 끝이 난다

    array[i], array[min_index] = array[min_index], array[i]

print(array)

# def sel_sort(a):
#     n = len(a)
#
#     for i in range(0, n - 1):
#
#         min_idx = i
#
#         for j in range(i + 1, n):
#
#             if a[j] < a[min_idx]:
#                 min_idx = j
#
#         a[i], a[min_idx] = a[min_idx], a[i]
#
#         print(a)  # 정렬 과정 출력하기
#
#
# d = [4, 2, 5, 1, 3]
#
# sel_sort(d)
#
# print(d)