def reqursive(search_list,target):
    if len(search_list) == 0:
        return False

    midpoint = (len(search_list)) // 2
    if search_list[midpoint] == target:
        return True
    else:
        if (search_list[midpoint] < target):
            return reqursive(search_list[midpoint+1:],target)
        elif search_list[midpoint] > target:
            return reqursive(search_list[:midpoint],target)

def verify(result):
    print(f"Target Found: {result}")


numbers = [1,2,3,4,5,6,7,8,9,10]

result1 = reqursive(numbers, 6)
verify(result1)

result2 = reqursive(numbers, 3)
verify(result2)