# Initialize variables

x = 5     # Integer variable x starts at 5

y = 1.1   # Float variable y starts at 1.1

z = True   # Boolean variable z is True, used for the loop

z_count = 0    # Initialize counter for z

teksts = 'Hello everyone'	# String variable containing a greeting

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	# List of integers from 1 to 10

a = 2   # Integer variable a starts at 2

b = 1000        # Integer variable b starts at 1000

# Iterate over each item in the list

for i in list:        
	
	x = x + i	# Add current item to x

        y = y - i	# Subtract current item from y

        a = a * i	# Multiply a by the current item

        b = b / i	# Divide b by the current item

# Conditional checks after the loop

if x >= 10:

        print(x)	# Print x if it is greater than or equal to 10

if y < 0:

	print(y)	# Print y if it is less than 0

if a != 2:

	print(a)	# Print a if it is not equal to 2

if b == 0:

	print(b)	# Print b if it is equal to 0

# Count to five using a while loop

print('Lets count to five')	# Print message before counting

while z:	# While z is True

	z_count += 1	# Increment z_count by 1

	print(f'Counted to {z_count}')	# Print the current count 

	if z_count >= 5:	# If count exceeds 5

		z = False	# Set z to False to exit the loop

print('Counted to 5')	# Print message after finishing the count

# String manipulation

one = teksts[11:]	# Get substring from index 11 to the end

hell = teksts[:4]	# Get substring from the start to index 4 (exclusive)

everyone = teksts[6:]	#Get substring from index 6 to the end

#Print concatenated result

print(one + ' ' + hell + ' for ' + everyone) 

print("help")
