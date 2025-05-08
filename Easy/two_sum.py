def two_sum(nums, target):
    for first_index in range(0, len(nums) - 1):
        for second_index in range(first_index + 1, len(nums)):
            if nums[first_index] + nums[second_index] == target:
                return [first_index, second_index]