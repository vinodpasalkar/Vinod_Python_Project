'''
Created on 22 May 2019

@author: vinod.pasalkar
'''
# Program to sort alphabetically the words form a string provided by the user

my_str = input("Enter a string: ")  

# breakdown the string into a list of words  
words = my_str.split()  
# sort the list  
words.sort()  
# display the sorted words  
print("The sorted words are:")
for word in words:  
   print(word)  