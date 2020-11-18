# puzzles

Puzzles for Thanksgiving break.

Have fun and give it your best shot!

These puzzles may be hard, and that's okay. Keep on giving it your best work, and you'll get it. Remember, Google and Stack Overflow are your friends.


***CONTENTS***

[Instructions](#instructions)

[Problems](#problems)

[Hints](#hints)

[Solutions](#my-solutions)


#### Instructions

Clone this repo either to your local machine or to Repl.it (https://repl.it/languages/python3). If you would like to save your work on Repl.it, make sure to sign in before visiting the link.

#### Problems

1: Write a Python program that:

    a) Prompts the user to write a list of words (for example, ['apple', 'mango', 'cashew']). 
    b) Once the list has been entered, the program will ask for a word to search for.
    c) The program will then say the number of times the word was found in the list, or display a message that the word wasn't found. For example: "___ was found 3 times" or "___ wasn't found."

The code for this program should be placed in the file 1.py. You may want to check the hints on this one, because there's some complicated input logic.



2:  Write another Python program that:

    a) Prompts the user to give a number, an INTEGER only.
    
    b) Prints every number up to the given number.
    
    c) Gives the time it took to print every number up to the user's number.
    
    The code for this program should be placed in the file 2.py


#### Hints:

**Puzzle 1**

Use the input function, as follows, to get the user's input of a list:

    user_list = list(map(input("Enter the list of strings you'd like to check... ").split()))

Remember that you can't use the variable "list" as it's already assigned to the basic Python language.

    list = list(map(input("Enter the list of strings you'd like to check... ").split()))

That won't work. You'll get an error.

Next, use an input function to ask the user what string to check for. This time, use a simple input function:

    check = input('Enter the string you'd like to check for... ')

Continue onward and work through it, using a for loop:

    if check in user_list:
        print(f'{check} is in the list!')
    else:
        print(f'{check} is not in the list.')

**Other Help**
Finally, if you have questions that you can't fix with Google, Stack Overflow, or these hints, text on the Slack (https://join.slack.com/t/dvgate/shared_invite/zt-ijp1fq2e-mi5WmevnbcgzzI6YefK9gQ). Follow the instructions to set up an account if you don't have one. Use the "puzzles" channel.


#### My Solutions
