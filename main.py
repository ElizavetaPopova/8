def kbig(nums, k):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i, len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[-k]