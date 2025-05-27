#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Write a program that prompts the user to enter a string and makes each alternate character into an uppercase character and each other alternate character a lowercase character.
string=input("Please enter a string comment.")
string_format = ''.join([string[i].upper() if i % 2 == 0 else string[i].lower() for i in range(len(string))])
print(string_format)


# In[38]:


#Now, try starting with the same string but making each alternative word lowercase and uppercase.
#e.g. The string “I am learning to code” would become “i AM learning TO code”.
#Tip: Using the split() and join() methods will help you here.
string_sentence=input("Please enter a string comment.")
string_sentence_split=string_sentence.split()
print(string_sentence_split) 
string_format2 = ' '.join([string_sentence_split[i].lower() if i % 2 == 0 else string_sentence_split[i].upper() for i in range(len(string_sentence_split))])
print(string_format2)

