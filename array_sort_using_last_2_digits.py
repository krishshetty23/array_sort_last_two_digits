# Hello, this is Krish J Shetty.
# Problem Statement: To sort an array of integers based on their last two digits

# Let us first take input from the user

array_inp = [int(x) for x in input("Enter multiple value: ").split(" ")]

# Let us se how our array looks like
print("Given Array:", array_inp)

# Now let us sort the array. Here, we have used the built-in function 'sorted'. However, we need the last two digits
# as the key to sort the array. For that purpose, we did k % 100 here because when we divide any number by 100,
# what we get as a remainder is the last two digits.

result = sorted(array_inp, key=lambda k: (k % 100, k))

# Here, what the lambda function does is, it takes all 'k's, i.e. all elements from the input array and creates tuples out of them. 
# The tuple consists of k % 100 and k itself. This tuple is then consumed by the dict() function, which 
# maps the two tuple elements as key:value pairs.

print("Sorted Array:", result)
