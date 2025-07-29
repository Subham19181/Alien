def linear_search(search_list,target):
    """
    Returns the index position of the target if found, else returns None.
    """
    for i in range(0, len(search_list)):
        if search_list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}.")
    else:
        print(f"Target not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result1 = linear_search(numbers,12)
verify(result1)

result2 = linear_search(numbers,6)
verify(result2)
