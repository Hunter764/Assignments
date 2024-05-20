#Prepends an element to the beginning of the dynamic array.
def prepend(arr,value):
    arr.insert(0,value)

arr=[1,2,3]
prepend(arr,0)
print(arr)