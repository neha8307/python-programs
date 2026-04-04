 def twoSum(nums, target):
    num_map = {}   # create empty dictionary

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

        print(twoSum(nums, target))
