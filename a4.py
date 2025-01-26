def multiple_tuple(nums):
    """Calculate the product of all numbers except the first one in the tuple."""
    if len(nums) < 2:
        return nums[0] if nums else None  
    product = 1
    for x in nums[1:]:  
        product *= x
    return nums[0], product 

try:
    user_input = input("Enter numbers separated by commas: ")
    nums = tuple(map(int, user_input.split(',')))
    
    print("\nOriginal tuple: ")
    print(nums)
    result = multiple_tuple(nums)
    
    if result:
        print("First number:", result[0])
        print("Product of the remaining numbers:", result[1])
    else:
        print("The tuple is empty.")
except ValueError:
    print("Error: Please enter a valid list of numbers separated by commas.")
