# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:46:33 2016

@author: yashvesikar
"""
#This is a project in an attempt to demonstrate the Collatz Conjecture
import pylab
user_input = int(input('please enter a number: '))
print(n)

def even(n):
    n = n/2
    return n

def odd(n):
    n = (3*n)+1
    return n

def draw_plot( x, y, plt_title, x_label, y_label):
    ''' Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis '''
    
    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    
    pylab.plot( x, y )
    pylab.show()
    
    

def maximum(dictionary):
    maximum = 0
    for k,v in dictionary.items():
        if v > maximum:
            maximum = dictionary[k]
    return maximum


D = {0:user_input}    
#calculations(n)
item = 0   

while user_input !=1:
    if user_input%2 == 0:
        user_input = even(user_input)
        item +=1
        D[item] = user_input
    
    elif user_input%2==1:
        user_input = odd(user_input)
        item+=1
        D[item] = user_input


    
steps = [k for k,v in D.items()]
value = [v for k,v in D.items()]
key_value = [(k,v) for k,v in D.items()]
key_value = sorted(key_value)

#for i in key_value[-10:]:
##    print(i)    
#    for k,v in steps,value:
#        print('{}    {}'.format(k,v))

#for k,v in D.items():
#    for i in range(10):
#        print('{}    {}'.format(k,v))

draw_plot(steps,value,'Collatz Representation','Step','Values')
print(maximum(D))