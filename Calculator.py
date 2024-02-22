#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Take user input for the first number
Number1 = int(input("Number 1: "))

# Display options(arithmetic operations)
print("\nChoose the operation you would like to perform:")
print("1. + (Addition)")
print("2. - (Subtraction)")
print("3. * (Multiplication)")
print("4. / (Division)")

# Take user input for operation choice
Choice = int(input("You chose: "))

# Determine the chosen operation
if Choice == 1:
    print("\nYou chose Addition")
elif Choice == 2:
    print("\nYou chose Subtraction")
elif Choice == 3:
    print("\nYou chose Multiplication")
elif Choice == 4:
    print("\nYou chose Division")
else:
    print("\nYou made an invalid choice!")

# Take user input for the second number
Number2 = int(input("\nNumber 2: "))

# Perform the operation based on the user's choice
if Choice == 1:
    print("The sum is:", Number1 + Number2)
elif Choice == 2:
    print("The difference is:", Number1 - Number2)
elif Choice == 3:
    print("The product is:", Number1 * Number2)
elif Choice == 4:
    if Number2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("The quotient is:", Number1 / Number2)

