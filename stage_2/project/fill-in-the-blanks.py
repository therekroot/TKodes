# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

easy = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in: __3__ "Hello __1__!" Of course, that isn't a very useful thing to do.
However, it is an example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.'''

samples = ['''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in: __3__ "Hello __1__!" Of course, that isn't a very useful thing to do.
However, it is an example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.''',

'''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in: __3__ "Hello __1__!" Of course, that isn't a very useful thing to do.
However, it is an example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.
It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.''',

'''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.''']


# The answer for ___1___ is 'function'. Can you figure out the others?
blanks = ['__1__','__2__','__3__','__4__']
answers = [['world','python','print'],['world','python','print','HTML'],['function','arguments','none','boolean']]
levels = ['easy','medium','hard']

def catch_non_int(value):
    try:
        integer = int(value)
        return integer
    except ValueError as e:
        print 'That is not an integer!'

def level_num_guesses():
    number = raw_input("Please enter an number of guesses you want per missing word (3 is suggested number): ")
    val = catch_non_int(number)
    while type(val) != int:
        number = raw_input("Please enter an integer for number of guesses you want per missing word (3 is suggested number): ")
        val = catch_non_int(number)
    return number

def text_difficulty():
    level = raw_input("Please enter difficulty of the text you must fill: " + levels[0] + ", " + levels[1] + ", or " + levels[2] + ": ").lower()
    while level not in levels:
        level = raw_input("Please enter a correct difficulty: " + levels[0] + ", " + levels[1] + ", or " + levels[2] + ": ")
    game_text = samples[levels.index(str(level))]
    return game_text

def word_missing(word,attempts,level_index):
    user_tries = 0
    while user_tries < attempts: #tries loop
        user_input = raw_input("Enter word for " + word + ": ") #require input
        if user_input.lower() == answers[level_index][blanks.index(word)]: #validate input is correct
            print("\n Correct! \n")
            return user_input.lower()
        user_tries += 1

        if user_tries == attempts: #if incorrect
            print("\n \n \n Game over. Please play again.")
            exit() #user loses the game, exit script
        print("\n Try Again. You have " + str(int(attempts) - user_tries) + " more attempt(s) \n")
    return word

def check_word(word,blanks): #function to check if word-part is in blanks
    for e in blanks:
        if e in word:
            return True
    return False

def trim_word(word,blanks): #function to check if word-part is in blanks
    for e in blanks:
        if e in word:
            return e
    return False

def fill_in_the_blanks(text,blanks,attempts):
    text_list = text.split()
    level_number = samples.index(text)
    for e in text_list:
        if e in text_list and check_word(e, blanks): #is e in updated text_list
            e_trim = trim_word(e,blanks)
            print text
            next_word = word_missing(e_trim,attempts,level_number)
            text = text.replace(e_trim,next_word) #replace ALL occurrences
            text_list = text.split()
    print(text)
    print("\n \n ************* \n Congratulations, you won! \n *************")
    return text

#if game has multiple text samples have function def play_game?
#from there level_selection will choose return a text index or reference

def play_game():
    print "\n \n Welcome to Fill In The Blanks! Follow the prompts to enter your difficulty settings. \n \n"
    attempts_total = level_num_guesses()
    sample = text_difficulty()
    fill_in_the_blanks(sample,blanks,attempts_total)
    return attempts_total


# check_word('___1___',blanks)
# fill_in_the_blanks(easy,blanks,3)
play_game()

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
