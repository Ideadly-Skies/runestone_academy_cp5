def bubble_sort(a_list):
    """sort the list using bubble sort algorithm"""
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                # exchange could be done as two simultaneous assignments
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j] 

def bubble_sort_short(a_list):
    """stop and recognize that the list is sorted"""
    for i in range(len(a_list)-1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                exchanges = True
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        if not exchanges:
            break
        
if __name__ == "__main__":
    a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    bubble_sort_short(a_list)
    print(a_list)