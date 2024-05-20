#Merges two dynamic arrays into a single dynamic array.

#M-1) '+'
def merge(arr1,arr2):
    return arr1+arr2

arr1=[1,2,3]
arr2=[4,5,6]
print(merge(arr1,arr2))

#M-2) extend() method
def exten(arr1,arr2):
    arr1.extend(arr2)
    return arr1
print(exten(arr1,arr2))
