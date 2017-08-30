#!/usr/bin/env python

name_list=['Mary', 'John']
print name_list
name=raw_input('Your name: ')
print ''
#print name
name_list.append(name)
print name_list

another_name_list= ['Fred']
print another_name_list

new_name_list = name_list + another_name_list
print new_name_list
