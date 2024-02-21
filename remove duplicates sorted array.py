def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    index = 2  # Position to insert the next non-duplicate element

    for i in range(2, len(nums)):
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1

    return index

# Test case
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
expectedNums = [0, 0, 1, 1, 2, 3, 3]
k = removeDuplicates(nums)
assert k == len(expectedNums)

print("Expected nums:", expectedNums)
print("Actual nums:", nums[:k])

for i in range(k):
    assert nums[i] == expectedNums[i]

print("Test Passed!")
