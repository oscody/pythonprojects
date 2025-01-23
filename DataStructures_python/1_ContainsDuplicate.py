


def containDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


input = [1,2,3,4]
print(containDuplicate(input))

input = [1,2,3,1]
print(containDuplicate(input))

input = [1,1,1,3,3,4,3,2,4,2]
print(containDuplicate(input))