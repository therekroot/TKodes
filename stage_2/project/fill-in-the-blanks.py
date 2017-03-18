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

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?
blanks = ['___1___','___2___','___3___','___4___']
answers = ['function','arguments','none','boolean']

def word_missing(word, blanks):
    attempts = 0
    while attempts < 3: #attempts loop
        user_input = raw_input("Enter word for " + word + ": ") #require input
        if user_input == answers[blanks.index(word)]: #validate input is correct
            print("\n Correct! \n")
            return user_input
        attempts += 1
        if attempts == 3: #if incorrect
            print("\n \n \n Game over. Please play again.")
            exit() #user loses the game, exit script
        print("\n Try Again. You have " + str(3 - attempts) + " more attempt(s) \n")
    return word

def check_word(word, blanks): #function to check if word-part is in blanks
    for e in blanks:
        if e in word:
            return True
    return False

def fill_in_the_blanks(text, blanks):
    text_list = text.split()
    for e in text_list:
        if e in text_list and check_word(e, blanks): #is e in updated text_list
            print(text)
            next_word = word_missing(e,blanks)
            text = text.replace(e,next_word) #replace ALL occurrences
            text_list = text.split()
    print(text)
    print("\n \n ************* \n Congratulations, you won! \n *************")
    return text


fill_in_the_blanks(sample,blanks)


# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
