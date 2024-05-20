#Deletes the element at the specified index.
def delete(arr,index):
    if 0 <=index<len(arr):
        del arr[index]
    else:
        raise IndexError("Index out of bounds")

arr=[1,2,3,4,5]
index=3
delete(arr,index)
print(arr)