from max_heap import parent
from max_heap import max_heapify

def heap_maximum(A):
    """Returns the maximum element of Max Heap"""
    return A[0]

def heap_extract_max(A, heap_size):
    """Return the largest element of heap"""
    if heap_size < 1:
        raise ValueError('Heap underflow')
    MAX = A[0]
    A[0] = A[heap_size-1]
    heap_size -= 1
    max_heapify(A, 0, heap_size)
    return MAX 

def heap_increase_key(A, i, key):
    """Increse the key of ith index by key value"""
    if key < A[i]:
        raise ValueError('New key is smaller than current key')
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i) 

def max_heap_insert(A, key, heap_size):
    """Insert key into heap"""
    heap_size += 1
    A[heap_size-1] = -9999
    heap_increase_key(A, heap_size, key)



