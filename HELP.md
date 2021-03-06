# Help.md for hints/solutions.

**Contents**

- [Hints](#hints)

    - [Puzzle 1](#puzzle-1-hints)
    
    - [Puzzle 2](#puzzle-2-hints)

    - [Puzzle 3](#puzzle-3-hints)
    
    - [More Help](#other-help)

- [Solutions](#my-solutions)

    - [Puzzle 1](#puzzle-1-solution)
    
    - [Puzzle 2](#puzzle-2-solution)



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
>>     while True:
>>         print(1)
>>         break

This will print the number 1 *one* time, then break the loop. Without the `break` line in the loop, it would print the number 1 forever unless stopped by external means.

The `x <= num` tells the program to run the loop as long as x is *less than* or *equal to* the user's input, `num`.

Then, finally, we'll add three lines of code to get the time it took to count:

    t2 = time.time()
    t3 = t2 - t1
    print(f'I told you so! It took {t3} seconds to count to {num}.')

The variable `t2` is the time *after* the loop has run its course. The variable `t3` actually is the time it was *before* the loop ***subtracted from*** the time it was *after* the loop. Then, it uses an `f` string to print how much time it took to count to the number it counted to.

After that, you're done! Good job. If you ran into any problems, go to the [Solutions](#my-solutions) section and check to see if you have it completely right.


###### Puzzle 3 Hints

To achieve the randomness of the number to guess, we'll need to import a module called `random`:

    import random

Then, we'll set the number that the player will have to guess:

    num = random.randint(0,100)

This calls a module function from `random` to get a random number in a range.

Next, we set up the variable `tries` to make sure that we can count the number of tries:

    tries = 0

After this, we'll set up our `while` loop:

    while True:
        guess = input('Enter your guess... ')
        if guess > input:
            print('That number is too high. Try again!')
            tries += 1
        elif guess < input:
            print('That number is too low. Try again!')
            tries += 1
        elif guess == input:
            print('You guessed it right!')
            tries += 1
            break

The `while True` tells Python that until you break the loop with `break`, it should run this. Then, the variable `guess` is updated to get new user input. Directly afterwards, `if` and `elif` (which means *else if*, or basically do this regardless of whether or not the preceding condition applies). The logic tells the user if their guess is too low or too high, or if they guessed it right. It also adds 1 to `tries` for each guess.

Finally, we give the user their information:

    print(f'You did it! The number was {num} and it took you {tries} tries to guess it.)

And with that, you've completed the last puzzle.


###### Other Help
Finally, if you have questions that you can't fix with Google, Stack Overflow, or these hints, check out the solutions below.



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


###### Puzzle 3 Solution

    import random
    num = random.randint(0,100)
    tries = 0
    while True:
        guess = input('Enter your guess... ')
        if guess > input:
            print('That number is too high. Try again!')
            tries += 1
        elif guess < input:
            print('That number is too low. Try again!')
            tries += 1
        elif guess == input:
            print('You guessed it right!')
            tries += 1
            break
    print(f'You did it! The number was {num} and it took you {tries} tries to guess it.)