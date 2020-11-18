# Puzzles for Break
Puzzles for Thanksgiving break.

Have fun and give it your best shot!

These puzzles may be hard, and that's okay. Keep on giving it your best work, and you'll get it. Remember, Google and Stack Overflow are your friends.



***CONTENTS***

- [Instructions](#instructions)

- [Puzzles](#problems)

    - [Puzzle 1](#1-write-a-python-program-that)
    
    - [Puzzle 2](#2-write-another-python-program-that)

- [Hints](#hints)

    - [Puzzle 1](#puzzle-1-hints)
    
    - [Puzzle 2](#puzzle-2-hints)
    
    - [More Help](#other-help)

- [Solutions](#my-solutions)

    - [Puzzle 1](#puzzle-1-solution)
    
    - [Puzzle 2](#puzzle-2-solution)

- [Conclusion](#conclusion)



### Instructions

Clone this repo either to your local machine or to Repl.it (https://repl.it/languages/python3). If you would like to save your work on Repl.it, make sure to sign in before visiting the link. Remember to use the command `$ git clone https://github.com/peternielsen112/puzzles.git` in Git Bash. ***REMEMBER TO BE IN THE PROPER DIRECTORY.***



### Puzzles


###### 1: Write a Python program that:

> a) Prompts the user to write a list of words (for example, ['apple', 'mango', 'cashew']). 
    
> b) Once the list has been entered, the program will ask for a word to search for.
    
> c) The program will then say the number of times the word was found in the list, or display a message that the word wasn't found. For example: "___ was found 3 times" or "___ wasn't found."

The code for this program should be placed in the file 1.py. You may want to check the hints on this one, because there's some complicated input logic.


###### 2:  Write another Python program that:

> a) Prompts the user to give a number, an INTEGER only.
    
> b) Prints every number up to the given number.
    
> c) Gives the time it took to print every number up to the user's number.
    
The code for this program should be placed in the file 2.py



### Hints:


###### Puzzle 1 Hints

Use the input function, as follows, to get the user's input of a list:

    user_list = list(map(input("Enter the list of strings you'd like to check... ").split()))

Remember that you can't use the variable `list` as it's already assigned to the basic Python language.

    list = list(map(input("Enter the list of strings you'd like to check... ").split()))

That won't work. You'll get an error.

Next, use an `input` function to ask the user what string to check for. This time, use a simple input function:

    check = input('Enter the string you'd like to check for... ')

Continue onward and work through it, using `if` logic:

    if check in user_list:
        print(f'{check} is in the list!')
    else:
        print(f'{check} is not in the list.')

And that's it! You're done! Try running the program on Repl.it to see if it works. If it doesn't, look for any mistakes.



###### Puzzle 2 Hints

First, we'll import a module called `time`. Add this line of code to the *beginning* of the program:

    import time

After the import, we'll use the `input` function that we practiced in Puzzle 1:

    num = int(input('Enter any number, integer only... '))

Then, we'll set a variable (`x`) to `0`:

    x = 0

This is critical for counting to the user's number.

Then, add a line that sets a variable for use as referencing (we'll see it in use later):

    t1 = time.time()

The function `time.time()` uses the module `time` that we've imported and references a function within the module. The function is also called `time`. It gets the current time.

Now, we'll set up our logic:

    while x <= num:
        print(x)
        x += 1

You might not recognize some parts of this loop, for example, the `while x <= num`. The word `while` tells it to run this loop as long as the condition applies. Some examples include:

    while True:
        pass
    while not True:
        pass

>***NOTE:*** An important thing to know is the `break` command. When put inside a loop, it will break the loop instantly regardless of when the loop was specified to break. For example:
>
>>    `while True:`
>>        `print(1)`
>>        `break`

This will print the number 1 *one* time, then break the loop. Without the `break` line in the loop, it would print the number 1 forever unless stopped by external means.

The `x <= num` tells the program to run the loop as long as x is *less than* or *equal to* the user's input, `num`.

Then, finally, we'll add three lines of code to get the time it took to count:

    t2 = time.time()
    t3 = t2 - t1
    print(f'I told you so! It took {t3} seconds to count to {num}.')

The variable `t2` is the time *after* the loop has run its course. The variable `t3` actually is the time it was *before* the loop ***subtracted from*** the time it was *after* the loop. Then, it uses an `f` string to print how much time it took to count to the number it counted to.

After that, you're done! Good job. If you ran into any problems, go to the [Solutions](#my-solutions) section and check to see if you have it completely right.


###### Other Help
Finally, if you have questions that you can't fix with Google, Stack Overflow, or these hints, text on the Slack [(sign up here)](https://join.slack.com/t/dvgate/shared_invite/zt-ijp1fq2e-mi5WmevnbcgzzI6YefK9gQ). Follow the instructions to set up an account if you don't have one. Use the "puzzles" channel.


### My Solutions


###### Puzzle 1 Solution

    user_list = list(map(input("Enter the list of strings you'd like to check... ").split()))
    check = input('Enter the string you'd like to check for... ')
    if check in user_list:
        print(f'{check} is in the list!')
    else:
        print(f'{check} is not in the list.')


###### Puzzle 2 Solution

    import time
    num = int(input('Enter a number, integer only... ')
    x = 0
    t1 = time.time()
    while x <= num:
        print(x)
        x += 1
    t2 = time.time()
    t3 = t2 - t1
    print(f'I told you so! It took {t3} seconds to count to {num}.')

### Conclusion

In these puzzles, you learned basic logic of `if`, `else`, and `while`. You also learned about modules, and more specifically, the `time` module and how to use it, if at least minimally. You learned about `f` strings and you built two programs that created specific functions. After break, we'll do more in Python and work through how to create more complex problems.
