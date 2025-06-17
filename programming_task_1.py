# This code takes a list of integers for example [8,3,5,1], and converts it to an integer, in this case 8351.
# We go through every integer inside the list from left to right and somehow want to build a numerical result from it
# For every integer in the list we do the following
#   Get the current result, and multiply it by 10 to create 'space' for the digit to be added
#   Then, we add the digit to the result
# In the end, we will end up having an integer such that every digit is an element from a given list from left to right

# Uncomment the lst which you want to test
# lst = [1, 1, 1]
# lst = [7, 2, 9, 0, 1, 4, 2, 8]
# lst = [6]

lst = [8, 3, 5, 1]
result: int = 0 # This will be the integer we want to represent at the end
for digit in lst:
    result = result * 10 + digit # For each digit we want to 'append' to the result, we create space for it by multiplying it by 10, then we add the desired digit

print(result)







