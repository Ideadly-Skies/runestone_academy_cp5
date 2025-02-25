def binary_search(a_list, item):
    """iterative approach"""
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False

def binary_search_rec(a_list, item):
    """recursive approach using divide and conquer algorithm"""
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    elif item < a_list[midpoint]:
        return binary_search_rec(a_list[:midpoint], item)
    else:
        return binary_search_rec(a_list[midpoint+1:], item)

if __name__ == "__main__":
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

    print(binary_search(test_list, 3))  # false
    print(binary_search(test_list, 13)) # true

    print(binary_search_rec(test_list, 3))  # false
    print(binary_search_rec(test_list, 13)) # true