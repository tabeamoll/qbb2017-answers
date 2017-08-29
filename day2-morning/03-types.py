#!/usr/bin/env python

print "Basic types..."

a_string = "This is a string"

an_integer = 7

i_as_s = str( an_integer )

a_real = 5.689

s_as_real = float ("5.689")

truthy = True
falsy = False

for value in a_string, an_integer, a_real, truthy: print value, type (value)

print "Lists and Tuples"

a_list = [1, 2, 3, 4, 5]
a_tuple = (1, "foo", 3.2)

print a_list, type (a_list)
print a_tuple, type(a_tuple)

#lists are mutable
a_list[3] = 777
print a_list

#Tuples are NOT
##Following lines will output an Error
##a_tuple[3]=777
##print a_tuple

#if you type another_list = a_list you share the same list with both names, modifying another_list automatically modifies a_list ; this applies for all mutable variables
another_list = list(a_list)

another_list[3] = 888
print another_list

print a_list