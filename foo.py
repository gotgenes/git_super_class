#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

user_name = sys.argv[1]

if len(sys.argv) < 2:
    print "Usage: foo.py YOURNAME."
    sys.exit()

print "Hello, {}!".format(user_name)
print "The sum of 2 and 3 is: {}".format(2 + 3)
print "I like Git!"
