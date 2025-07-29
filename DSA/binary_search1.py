def binary_search(search_list,target):
    first = 0
    last = len(search_list) - 1

    while first <= last:
        midpoint = (first + last) // 2 #double '/' rounds *DOWN* the division to an int value. ex: 101//2 = 50 NOT 51

        #if midpoint value is the target:
        if search_list[midpoint] == target:
            return midpoint

        #if mid_value is LESS than target then we redefine our first var
        elif search_list[midpoint] < target:
            first = midpoint + 1 #it is +1 cause the midpoint cant be the target(if it was the upper if statement would be executed)

        elif search_list[midpoint] > target:
            last = midpoint - 1 #it is -1 cause the midpoint cant be the target(if it was the upper if statement would be executed)

    #if any value existed in the list
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}.")
    else:
        print(f"Target not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result1 = binary_search(numbers,12)
verify(result1)

result2 = binary_search(numbers,6)
verify(result2)