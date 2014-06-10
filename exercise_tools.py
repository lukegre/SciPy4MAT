# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:44:25 2013

@author: Luke
"""

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)



def print_sublists(list):
    """This function prints a nice representation of objects inside a list"""
    # if "\t" is printed as a string, it prints a tab space, similarly
    # if "\n" is printed as a string, it denotes a new line
    print '== A NICER REPRESSENTAION =='
    print 'Index\tLength\tObject Type'
    for i in range(len(list)):
        print '%d\t' % i,
        try:  # the try function is amazing! Ask me about it
            print '%d\t' % len(list[i]),
        except:
            print 'NA\t',
        print str(type(list[i]).__repr__)[29:-10]
    print '==========================='


def avail_methods(list, excl='_', incl=''):
    method_list = []
    for method in list:
        if (not method.startswith(excl)) & \
           (method.startswith(incl)):
            method_list.append(method)
    print method_list


if __name__ == '__main__':
    print 'excercise tools running as main'
    print __file__
