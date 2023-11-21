def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if the current number is the start of a sequence
            current_num = num
            current_sequence = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(nums)
print("Length of the longest consecutive elements sequence:", result)
