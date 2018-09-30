def selectionSort(arr):
    for i in range(len(arr)):
        minima = arr[i]
        min_ind = i
        for j in range (i+1, len(arr)):
            if arr[j] < minima:
                minima = arr[j]
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
string = input().split(" ")
data = [int(item) for item in string]
selectionSort(data)
print(data)