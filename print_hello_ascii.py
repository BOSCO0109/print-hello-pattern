# print-hello-pattern
#This Python script prints the word "HELLO" using ASCII characters and nested loops. It demonstrates the use of conditional logic, for loops, and pattern printing in a creative way. Ideal for beginners learning Python control structures and character-based output.


# This code is show us the usage of union , and ,not ,or and else function  
# using the range and len function

for row in range(7):
    for col in range (5):
        if (row==3) or (col==0 or (col==4)):                   #H word
            print('#',end='')
        else:
            print(' ',end='')
    print(' ',end='')
    for col in range (5):
        if (row==0 or row==3 or row==6) or (col==0):            #E word
            print('#',end='')
        else:
            print(' ',end='')
    print(' ',end='')
    for col in range (5):
        if (row==6 or col==0):                                  #L word
            print('#',end='')
        else:
            print('',end=' ')
    print(' ',end='')
    for col in range (5):
        if (row==6 or col==0):                                  #L word
            print('#',end='')
        else:
            print('',end=' ')
    print(' ',end='')
    for col in range(5):
        if (row==0 or row==6) or (col==0 or col==4):            #0 word
            print('#',end='')
        else:
            print('',end=' ')
    print() 
    
