import random
def bubble_sort(list_to_sort):
    list_len = len(list_to_sort)

    for i in range(list_len):
        for j in range(list_len - 1):
            if list_to_sort[j]<list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

    return list_to_sort




if __name__ == "__main__":
    list_sort = random.choices(range(101), k=50)

    
    bubble_sort(list_sort)
    print("Sorted: ")
    print(list_sort)

    