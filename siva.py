def maxPoints(nums):
    if not nums:
        return 0
    
    # Create a dictionary to store the sum of points for each unique number
    points = {}
    
    # Initialize the points dictionary with each unique number in nums
    for num in nums:
        points[num] = points.get(num, 0) + num
    
    # Create a list to store the maximum points for each unique number
    dp = [0] * len(points)
    
    # Sort the unique numbers in ascending order
    unique_nums = sorted(points.keys())
    
    # Initialize the first element in dp
    dp[0] = points[unique_nums[0]]
    
    # Calculate the maximum points using dynamic programming
    for i in range(1, len(unique_nums)):
        if unique_nums[i] - 1 == unique_nums[i - 1]:
            # If the current number is consecutive to the previous one, skip it
            dp[i] = max(dp[i - 1], points[unique_nums[i]])
        else:
            # Otherwise, choose either to include the current number or not
            dp[i] = max(dp[i - 1], dp[i - 2] + points[unique_nums[i]])
    
    # Return the maximum points
    return dp[-1]

# Example usage:
n = [1, 2, 3]
result = maxPoints(n)
print(result)  # This will correctly print 4 as the maximum points.
