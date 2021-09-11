#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyperclip, re

def checkPassword():
    lengthRegex =  re.compile(r'(.{8,})') # checks to be at least 8 characters
    checkUpper = re.compile(r'([A-Z]+)')  #checks for uppercase
    checkLower = re.compile(r'([a-z]+)') #checks for lower
    checkNumber = re.compile(r'([0-9]+)')  #checks for a number
    checkSymbols = re.compile(r'([!@#$%^&*]+)')   #checks for a symbol
    validPassword = []
   

    password = str(pyperclip.paste())
    for groups in lengthRegex.findall(password): #creates a list that will be checked for valid characters
        validPassword.append(groups)
   
    
   #checks the list for valid passwords
    for i in validPassword:
        for groups in checkNumber.findall(i) and checkSymbols.findall(i) and checkLower.findall(i) and checkUpper.findall(i):
            print(i + ' is a valid password')
            break
                    

       
            
    
    
checkPassword()

