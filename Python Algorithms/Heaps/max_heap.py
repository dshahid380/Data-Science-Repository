def parent(i):
    """Returns the index of parent"""
    return(i//2)

def right(i):
    """Returns the index of right child of node"""
    return(2*i+2)

def left(i):
    """Returns the index of left child"""
    return(2*i+1)

def max_heapify(A, i, heap_size):
    """Whenever it is called, the largest of A[i], A[left(i)] and A[right(i)] is
    determined, and its index is stored in largest. If A[i] is largest, then the
    subtree rooted at node i is already a max heap and the procedure terminates.
    Otherwise, one of the two children has the largest element, and A[i] is swapped
    with A[largest], which cause node i and its children to satisfy the heap-property."""
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i 

    if r < heap_size and A[r] > A[largest]:
        largest = r 

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    """Building max heap using heapify function"""
    heap_size = len(A)
    for i in range(heap_size, -1, -1):
        max_heapify(A, i, heap_size)
     
def heapsort(A):
    """First build the max heap then return the sorted array"""
    
    heap_size = len(A)
    #Build Max Heap
    build_max_heap(A)
     
    #Sorting
    for i in range(len(A)-1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        max_heapify(A, 0, i)

    return A 

#Test
A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

#Printing sorted array
print(heapsort(A))

#Output
[1, 2, 3, 4, 7, 8, 9, 10, 14, 16]





