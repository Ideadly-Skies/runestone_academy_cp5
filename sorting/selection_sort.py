def selection_sort(a_list: list):
    """select the largest number on each pass and place them on the correct position"""
    for i in range(len(a_list)-1, 0, -1):
        max_idx = 0 # holds the max_idx of the list for each pass 
        for j in range(i, 0, -1):
            if a_list[j] > a_list[max_idx]: # if a_list[j] > a_list[max_idx] (set max_idx to j)
                max_idx = j
        if max_idx != i:
            a_list[max_idx], a_list[i] = a_list[i], a_list[max_idx] # swap the position

if __name__ == "__main__":
    """run the selection sort function in here"""
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(a_list)
    print(a_list)