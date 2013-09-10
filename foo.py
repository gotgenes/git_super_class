#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

if len(sys.argv) < 2:
    print "Usage: foo.py YOURNAME."
    sys.exit()

print "Hello, {}!".format(sys.argv[1])
print "The sum of 2 and 3 is: {}".format(2 + 3)
print "I like Git!"
