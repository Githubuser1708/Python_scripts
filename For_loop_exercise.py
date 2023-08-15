# Exercise: 7-Up
# Create a list containing the nmber 1 to 100. Then loop through the list to replace multiples of 7 with '7-Up'
# Also replace any numbers containing the digit 7 with '7-Up'.


# Step 1: generate a list of numbers from 1 to 100
numlist = list(range(1, 101))
print(numlist)

# Step 2: loop through this list using for loop
for i in range(len(numlist)):

    # Step 3: if the element is a multiple of 7 or contains the digit 7, replace with '7-Up'
    if numlist[i] % 7 == 0 or "7" in str(numlist[i]):
        numlist[i] = '7-Up!'

print(numlist)