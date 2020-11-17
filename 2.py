# puzzle 2


# in this puzzle, you'll need to make a loop that prints every number in a user's input.


def debug():
  try:
    import time, os, sys, random
    # you might not need all these modules for this puzzle, but you'll have to figure it out!
  except ImportError:
    print('Your modules didn\'t import correctly... try fixing your spelling!')
debug()


# start with setting a variable, x, to zero:
x = 0
userinput = input('prompt')


# here's some pseudocode (basically showing what you want to happen) on how to make the loop:
'''
while x is less than user's input:
  print x
  add one to x
'''

while x <= userinput:
  pass
