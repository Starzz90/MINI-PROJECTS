def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ask for user input
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert the input to integers

# Sort the list
bubble_sort(numbers)

# Display the sorted numbers
print("Sorted numbers:", numbers)
