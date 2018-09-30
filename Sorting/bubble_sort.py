def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range (len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
string = input().split(" ")
data = [int(item) for item in string]
bubbleSort(data)
print(data)