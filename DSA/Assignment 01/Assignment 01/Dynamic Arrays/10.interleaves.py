#Interleaves two dynamic arrays into a single dynamic array.
def interleave(arr1,arr2):
    interleave=[]
    min_len=min(len(arr1),len(arr2))

    for i in range(min_len):
        interleave.append(arr1[i])
        interleave.append(arr2[i])

    interleave.extend(arr1[min_len:])
    interleave.extend(arr2[min_len:])

    return interleave

arr1=[1,2,3,4]
arr2=[5,6,7,8]
print(interleave(arr1,arr2))