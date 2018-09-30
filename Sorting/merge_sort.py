def merge(arr, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r - m)
    L = [0] * n1
    R = [0] * n2
    for i in range (n1):
        L[i] = arr[l + i]
    for j in range (n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = int((l + (r - 1))/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

string = input().split(" ")
data = []
for x in string:
    data.append(int(x))
mergeSort(data, 0, len(data)-1)
print (data)