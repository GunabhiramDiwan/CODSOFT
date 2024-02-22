#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length):
    # Define the characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

