# Activities:

# Coding Exercise:
# Write a function that uses two nested loops to check each element against all others for duplicates.
# Add comments to explain each part of your code.
# Run the code with different input sizes to observe performance.
# Homework:

# Modify the brute-force code to count how many times each duplicate occurs.
# Write a brief summary of the time complexity of your solution.



def BruteForce(nums):
    # Outer loop: Iterate over each element in the list by index 'i'
    for i in range(len(nums)):
        # Inner loop: Iterate over the elements after index 'i' by index 'j'
        for j in range(i + 1, len(nums)):
            # Compare the element at index 'i' with the element at index 'j'
            if nums[i] == nums[j]:
                # If a duplicate is found, print a message and return True
                print(f"Duplicate found: {nums[i]} at positions {i} and {j}")
                return True  # Exit the function as we have found a duplicate
    # If no duplicates are found after checking all elements, return False
    print("No duplicates found.")
    return False
        

if __name__ == "__main__":

    nums = [2,3,5,6,2,4,5]
    BruteForce(nums)

