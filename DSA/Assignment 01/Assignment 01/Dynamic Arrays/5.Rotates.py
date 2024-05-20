#Rotates the dynamic array by k positions to the right.
def rotate(arr,k):
    if not arr:
        return arr
    k=k%len(arr)
    return arr[-k:]+arr[:-k]

arr=[1,2,3,4,5,6]
k=2
print(rotate(arr,k))