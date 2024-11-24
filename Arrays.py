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

''' *****   Next Permutation   *****   '''
# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation.
# If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Steps to do:

# -> Iterate over the given array from end and find the first index (pivot) which doesn’t follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1]).
# -> If pivot index does not exist, then the given sequence in the array is the largest as possible. So, reverse the complete array. For example, for [3, 2, 1], the output would be [1, 2, 3]
# -> Otherwise, Iterate the array from the end and find for the successor (rightmost greater element) of pivot in suffix.
# -> Swap the pivot and successor
# -> Minimize the suffix part by reversing the array from pivot + 1 till n.

#Time Complexity of this is - O(n)
def nextPermutation(arr):
        # Python Program to find the next permutation by generating only next
        n = len(arr)
        
        # Find the pivot index
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        
        # If pivot point does not exist, reverse the whole array
        if pivot == -1:
            arr.reverse()
            return
    
        # Find the element from the right that is greater than pivot
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
    
        # Reverse the elements from pivot + 1 to the end in place
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [1,53,8,2,7]
nextPermutation(arr)
print(arr)

#Other way with time complexity: O(n!)
import itertools

def nextPermutation(arr):
    # Find all permutations of the array and sort them
    perms = sorted(itertools.permutations(arr))
    
    # Find the index of the current permutation
    current_index = perms.index(tuple(arr))
    
    # Return the next permutation if it exists; otherwise, return the first permutation (sorted order)
    next_perm = perms[current_index + 1] if current_index + 1 < len(perms) else perms[0]
    
    # Convert the tuple back to a list and update arr
    arr[:] = list(next_perm)

arr = [1, 53, 8, 2, 7]
nextPermutation(arr)
print(arr)

""" *****   Majority of Element(n/3)   *****   """
# You are given an array of integer arr[] where each number represents a vote to a candidate.
# Return the candidates that have votes greater than one-third of the total votes
# If there's not a majority vote, return an empty array. 

#Time Complexity:O(n)

def majority(arr):
    n = len(arr)
    freq = {}
    result = []
    for element in arr:         #Find frequency of each number
        freq[element] = freq.get(element,0) + 1
    
    for element, count in freq.items():
        if count > (n // 3):
            result.append(element)

    result.sort()
    return result

arr = [3,7,7,7,9,9,9,1]
result = majority(arr)
print(result)

# Second way with time complexity : O(n logn)
from collections import Counter

def maj_element(arr):
    n = len(arr)
    frequency = Counter(arr)
    result = [element for element, count in frequency.items in arr if count > (n//2)]
    result.sort()
    return result

arr = [3,7,7,7,9,9,9,1]
result = majority(arr)
print(result)

''' *****   Stock Buy and Sell  *****   '''
#The cost of stock on each day is given in an array price[]. 
#Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day. 
# Find the maximum profit that you can get.

#Time Complexity : O(n)

def max_profit(prices):
    result = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            result += prices[i] - prices[i - 1]

    return result

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(max_profit(prices))

""" *****Stock Buy and Sell – Max one Transaction Allowed *****   """
# The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. 
# Here one transaction means 1 buy + 1 Sell.
# If it is not possible to make a profit then return 0.

def max_one_profit(price):
    min_price = price[0]
    result = 0

    for i in range(1,len(price)):
        min_price = min(min_price, price[i])      # Update the minimum value seen so far if we see smaller

        result = max(result, price[i] - min_price)# Update result if we get more profit 
    
    return result

price = [7, 10, 1, 3, 6, 9, 2]
print(max_one_profit(price))

'''Minimize the Heights'''
#Given an array arr[] denoting heights of N towers and a positive integer K.
#For each tower, you must perform exactly one of the following operations exactly once.

#  -> Increase the height of the tower by K
#  -> Decrease the height of the tower by K
#Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.


def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()
    
    initial_diff = arr[-1] - arr[0]
    result = initial_diff
    
    for i in range(n - 1):
        max_height = max(arr[-1] - k, arr[i] + k)
        min_height = min(arr[0] + k, arr[i + 1] - k)
        
        if min_height < 0:
            continue
        
        result = min(result, max_height - min_height)
    
    return result

arr = [3, 9, 12, 16, 20]
k = 3
diff = get_min_diff(arr, k)
print(diff)

''' *****    KADANE'S ALGOROTIHM ******'''
# Given an integer array arr[]. You need to find the maximum sum of a subarray.

def maximum_arr(arr):
    result = arr[0]
    max_end = arr[0]

    for i in range(1,len(arr)):
        max_end = max(max_end + arr[i] , arr[i])
        result = max(result, max_end)
    return result

arr = [2, 3, -8, 7, -1, 2, 3]
print(maximum_arr(arr))