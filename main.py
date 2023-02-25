def sortAscending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def sortDescending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    nums = input("Enter a list of numbers, separated by commas: ")
    num_list = [int(num) for num in nums.split(",")]

    sort_order = input("Enter 'asc' for ascending sort, or 'desc' for descending sort: ")

    if sort_order == "asc":
        sorted_list = sortAscending(num_list)
    elif sort_order == "desc":
        sorted_list = sortDescending(num_list)
    else:
        print("Invalid input. Please enter 'asc' or 'desc'.")

    print(sorted_list)