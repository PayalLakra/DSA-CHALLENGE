''' *****   Second Largest element of an Array  *****   '''

# Goal: The Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.
# Note: If the second largest element does not exist, return -1.
# Time Complexity for this is: O(n*logn)

def second_largest(arr):
    arr_set = list(set(arr))    # Remove duplicates by converting to a set, then back to a list
    arr_set.sort(reverse=True)  # Sort the array in descending order as by default sort function sort the array in ascending order

    if len(arr_set) < 2:
        return -1               # Return -1 if there aren't at least two unique elements
    else:
        return arr_set[1]       # This will print the 2nd largest element as it is present on 1st index.

arr = [8,93,1,4,7,90]
print(second_largest(arr))


# Second Approach: With time complexity O(n)
def largest_second(arr):
    n = len(arr)

    if n < 2:
        return -1

    largest = -1
    sec_largest = -1

    for i in range(n):    # First pass to get the largest element
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):    # Second pass to get the second largest element
        if arr[i] > sec_largest and arr[i] != largest:
            sec_largest = arr[i]
    return sec_largest

arr = [8,90,1,4,7,90]
print(largest_second(arr))




''' *****   Move All Zeroes to End *****    '''

# Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements.

# Time Complexity for this approach is O(n)
def pushZeroToEnd(arr):
    count = 0    # Pointer to track the position for next non-zero element
    
    for i in range(len(arr)):
        
        if arr[i] != 0:     # If the current element is non-zero
            arr[i], arr[count] = arr[count], arr[i]  # Swap the current element with the 0 at index count
            count += 1      # Move count pointer to the next position

arr = [1, 2, 0, 4, 3, 0, 5, 0]
pushZeroToEnd(arr)
print(arr)

# Second Approach with O(n) time complexity:
def push_zero(arr):
    count = 0

    for i in range(len(arr)):   # First loop: Traverse the array. If an element is non-zero, place it at the current count position
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1          # and then increment count to the next position.
    
    while count < len(arr):     # Second loop: Fill the remaining positions in the array with zeros from the 'count' position to the end of the array.
        arr[count] = 0
        count += 1

arr = [0,1,1,6,4,0,6,9,0]
push_zero(arr)
print(arr)

''' *****   Reverse an Array    *****   '''
# You are given an array of integers arr[]. Your task is to reverse the given array.

#Time Complexity : O(n)
def reverse_array(arr):
    rev_arr = arr[::-1]
    return rev_arr

arr = [1,2,5,9,3,4,5]
print(reverse_array(arr))


#Time Complexity : O(n)
def array_rev(arr):
    arr.reverse()
    return arr

arr = [1,2,5,9,3,4,5]
print(array_rev(arr))

''' *****   Rotate an Array *****   '''
#Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer.

# Reversal Algorithm with Time Complexity : O(n)

def rotate_array(arr,d):
    n = len(arr)
    if n < d:
        print("Not Possible to Rotate")
        return arr
    else:
        reverse(arr, 0, d-1)      #Reverse the first d elements
        reverse(arr, d, n-1)      #Reverse the remaining n-d elements
        reverse(arr, 0, n-1)      #Reverse the entire array
        return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7,8,9]
d = 3
print(rotate_array(arr,d))