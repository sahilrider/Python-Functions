def shellSort(arr):
    gap = int((len(arr)/2))
    while gap > 0:
        for i in range (gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap /= 2  
        gap = int(gap)
string = input().split(" ")
data = [int(item) for item in string]
shellSort(data)
print(data)