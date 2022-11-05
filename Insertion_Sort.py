def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
            for i in arr:
                print(i, end=' ')
            print()
        arr[j+1] = tmp
    for i in arr:
        print(i, end=' ')
