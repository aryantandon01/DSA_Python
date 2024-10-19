A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Heapify
import heapq
heapq.heapify(A)
print(A)

# Push
heapq.heappush(A, 4)
print(A)

# Pop
minn = heapq.heappop(A)
print(A, minn)

# Heapsort
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list
print(heapsort([1,3,5,7,9,2,4,6,8,0]))

# heappushpop
heapq.heappushpop(A, 99)
print(A)

#Max Heap
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range(n):
    B[i] = - B[i]
heapq.heapify(B)
print(B)
print([- i for i in B])  # This is the Max Heap
largest = - heapq.heappop(B)
print(largest)

heapq.heappush(B, -7) #Insert 7 into the Max Heap
print(B)

# Build Heap from scratch
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
print("\nHere is the construction of the heap step by step:")
for i in C:
    heapq.heappush(heap, i)
    print(heap)