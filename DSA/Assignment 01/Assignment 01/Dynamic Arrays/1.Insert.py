#Inserts an element at the specified index.
def insert_at(arr, index, value):
    if 0 <= index <= len(arr):
        arr.insert(index, value)
    else:
        raise IndexError("Index out of bounds")

arr = [1, 2, 3, 4, 5]
index = 2
value = 10

insert_at(arr, index, value)
print(arr)  #[1, 2, 10, 3, 4, 5]
