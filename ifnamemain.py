# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:49:41 2013

@author: Luke
"""
import os
from exercise_tools import avail_methods


def master():
    print 'master() function now running'

    other_function()


def other_function():
    print 'other function running from master()'

print "SCRIPT ACCESSED"
print "From namespace:\t%s" % __name__


if __name__ == "__main__":
    master()

    print
    from ifnamemain import other_function

if __name__ == os.path.splitext(__file__)[0]:
    print avail_methods(dir())
    