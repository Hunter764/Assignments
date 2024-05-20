#Reverses the dynamic array.

#M-1 -> Direct reverse function reverse()
def rev(arr):
    arr.reverse()

arr=[1,2,3]
rev(arr)
print(arr)

#M-2 -> Slicing method
def rev1(arr):
    return arr[::-1]

arr=[1,2,3,4]
print(rev1(arr))