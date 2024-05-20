#Returns true if the dynamic array is empty, false otherwise.
#M-1
def isempty(arr):
    return len(arr)==0
arr1=[]
arr2=[1]
print(isempty(arr1))
print(isempty(arr2))

#M-2
def isempty1(arr):
    return not arr

print(isempty1(arr1))
print(isempty1(arr2))