__author__ = "Priyanshu"
'''
9. WRITE A PROGRAM TO REPLACE A STRING WITH ANOTHER
   STRING WITHOUT USING .replace() (PAGE NO. 129)
'''

'''
  1. Define a function called 'replace' with parameters as
      i. currentString
      ii. old 
      iii. new
  
  2. Declare and assign empty string to 'newString'
  3. Use for loop to iterate through 'currentString' with iternation variable as 'word'
  4. Check if letter = old word from the parameter
      if True:
        append new word to 'newString'
      else: 
        append word to 'newString'
  5. Finally, return 'newString'
'''

def replace(currentString, old, new):
  newString = str() # empty string

  for word in currentString:
    if word is old[0]: # since 'letter' is single word
      newString += new
    else:
      newString += word

  return newString  # returning new string

# Examples & Limitations
print(replace('string', 's', 'S')) 
print(replace('He__o Wor_d', '_', 'l'))
print(replace('currentString', 'ur', '++')) 

'''
OUTPUT:
  String
  Hello World
  c++rrentString

'''


# Alternative method (4 lines)
'Below two function works similar to .replace()'

'''
  1. Define a function called 'replace' with parameters as currentString, old, new
  2. Declare and assign empty string to 'newString'
  3. From 'currentString', remove the old word(s), then
      i. We'll get a list
      ii. And with that list we'll assign to 'temp'
  4. Then we'll join the list with 'new' word(s) in their centers and assign it to 'newString'
  5. And finally we'll return 'newString'
'''


def replace(currentString, old, new):
  newString = str()

  # removing old words using .split(old)
  # adding new words in the middle
  temp = currentString.split(old)  
  newString = new.join(temp) 

  return newString

print(replace('Hello Wld Wld Wld', 'Wld', 'World'))
print(replace('Hello', 'l', 'new'))

# OUTPUT:
#   Hello World World World
  # Trace Back
  #   Value Error: empty separator


'''
  This method words same as the previous one.
  In this method, we're directly substituting and returning it.
'''

# Shortest Method (single line)
def replace(currentString, old, new):
  return new.join(currentString.split(old))

print(replace('Hello Wld Wld Wld', 'Wld', 'World'))

# OUTPUT:
#   Hello World World World


'''
Normal method:
  1. Define a function called 'replace' with parameters as
      i. currentString
      ii. old 
      iii. new
  
  2. Declare and assign empty string to 'newString'
  3. Use for loop to iterate through 'currentString' with iternation variable as 'word'
  4. Check if letter = old word from the parameter
      if True:
        append new word to 'newString'
      else: 
        append word to 'newString'
  5. Finally, return 'newString'

Alternative method:
  1. Define a function called 'replace' with parameters as currentString, old, new
  2. Declare and assign empty string to 'newString'
  3. From 'currentString', remove the old word(s), then
      i. We'll get a list
      ii. And with that list we'll assign to 'temp'
  4. Then we'll join the list with 'new' word(s) in their centers and assign it to 'newString'
  5. And finally we'll return 'newString'

Shortest method:
  This method words same as the previous one.
  In this method, we're directly substituting and returning it.

The Alternative and Short method is similar to str.replace() method.
'''