def create_array():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)
    return arr

def display(arr):
    print("Current Array:", arr)

def insert_element(arr):
    pos = int(input("Enter position to insert: "))
    val = int(input("Enter value: "))
    arr.insert(pos, val)

def delete_element(arr):
    val = int(input("Enter value to delete: "))
    if val in arr:
        arr.remove(val)
        print("Deleted successfully.")
    else:
        print("Value not found.")

def search_element(arr):
    val = int(input("Enter value to search: "))
    if val in arr:
        print(f"Element {val} found at index {arr.index(val)}")
    else:
        print("Element not found.")

# Driver Code
arr = create_array()

while True:
    print("\n1.Display  2.Insert  3.Delete  4.Search  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: display(arr)
    elif ch == 2: insert_element(arr)
    elif ch == 3: delete_element(arr)
    elif ch == 4: search_element(arr)
    elif ch == 5: break
    else: print("Invalid choice!")
