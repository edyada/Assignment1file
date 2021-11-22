#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to count the number of even and odd numbers from a series of numbers.



Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 4

Number of odd numbers : 5


# In[4]:


list1 = [1,2,3,4,5,6,7,8,9]
even_count, odd_count = 0, 0
for num in list1:
    if num % 2 == 0:
        even_count += 1
        
    else:
        odd_count += 1
        
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count )


# In[5]:


numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for num in numbers:
    if not num % 2:
        count_even+=1
        
    else:
        count_odd+=1

print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[11]:


l = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
odd_count = 0
for i in l:
    if i % 2 != 0:
        odd_count += 1
        print(i,"is odd number")
    else:
        even_count += 1
        print(i,"is Even number")
    
print("Numbers of even number in the list is :",even_count)
print("Numbers of odd number in the list is ",odd_count)


# In[ ]:





# In[ ]:




