def sequential_search(ls: list, num_to_search: int):
    for num in ls: # O(n) in the worse case
        if (num == num_to_search):
            return True
    return False

if __name__ == "__main__":
    print(sequential_search([1,2,3,4,5,6], -6))