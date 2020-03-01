def act(nums):
    nums = nums[::-1]
    print(nums)
    return nums

def run(nums):
    x = nums[:]
    print(f"Before act: {x}")
    x = act(x)
    print(f"After act: {x}")

x = [1, 2, 3, 4, 5]
run(x)