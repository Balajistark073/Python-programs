'''input_array = [1, 7, -3, -4, 5, 6, 9, 10, -21, -81]
subarrays = []
subarraysum = []
for i in range(len(input_array)):
    for j in range(i + 1, len(input_array) + 1):
        subarrays.append(input_array[i:j])
for subarray in subarrays:
    subarray_sum = sum(subarray)
    subarraysum.append(subarray_sum)
max_subarray_sum = max(subarraysum)
print("Maximum Subarray Sum:", max_subarray_sum)'''

def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = 0
    temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    return max_so_far, arr[start:end+1]
input_array = [1, 7, -3, -4, 5, 6, 9, 10, -21, -81]
max_subarray_sum, max_subarray = max_subarray_sum(input_array)
print("Maximum Subarray:", max_subarray)
print("Maximum Subarray Sum:", max_subarray_sum)
