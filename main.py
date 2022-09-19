# import random module
import random
import math
# set starting score
score = 0
counter = 0
# create list for total score
# user inputs how they would like to start off the game
userStart = int(input(
    "Press 1 to read the instructions of the game and Press 2 to begin the game!"))
# create function and set parameters for addition operator


def addition(score):
    # sets counter for addition round
    counter = 0
# creates while loop for iteration until program is terminated once conditions are met
    while counter < 3:
        # generates random numbers
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
# print randomly chosen numbers to user
        print(num1)
        print(num2)
# user inputs answer to problem
        userAnswer = int(input("Add: "))
# sets conditions for if user answers question correctly
        if userAnswer == num2+num1:
            # increases score if question is answered correctly
            score = score + 10
            counter = counter + 1
# prints new score after each question # ALL DONE
            print("Score:", score)
# if 3 or more questions are answered correctly user moves on to next round
            if counter >= 3:
                if score > 200:
                    print("Congrats! You have won the game. Press 2 to play again.")
                else:
                    print("Your score after the round is", score)
                    print("Next Round, Subtract:")
                    subtraction(score)
    # creates else statement to set conditions for if user answers question incorrectly
        else:
            counter = 0
            print("Incorrect")
# takes away point if user answers question incorrectly
            score = score - 5
            print("Score:", score)

# create function  and set parameters for subtraction operator


def subtraction(score):
    # sets counter for subtraction round
    counter = 0
# creates while loop for iteration until program is terminated once conditions are met
    while counter < 3:
        # generate random numbers
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
# print randomly chosen numbers to user
        print(num1)
        print(num2)
# user inputs answer to problem
        userAnswer = int(input("Your answer:"))
# sets conditions for if user answers question correctly
        if userAnswer == num1-num2:
            counter = counter + 1
# increases score if question is answered correctly
            score = score + 10
# prints new score after each question
            print("Score:", score)
# if 3 or more questions are answered correctly user moves on to next round
            if counter >= 3:
                if score > 200:
                    print("Congrats! You have won the game. Press 2 to play again.")
                    game(userStart)
                else:
                    print(
                        "Moving onto the next round!! Your score after this round is", score)
                    squared(score)
# creates else statement to set conditions for if user answers question incorrectly
        else:
            print("Incorrect")
# takes away points if user answers question incorrectly
            score = score - 5
            print("Score:", score)

# create function and set parameters for multiplication operator


def multi(score):
    # sets counter for multiplication round
    counter = 0
# creates while loop for iteration until program is terminated once conditions are met
    while counter < 3:
        # generate random numbers
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
# print randomly chosen numbers to user
        print(num1)
        print(num2)
# user inputs answer to problem
        userAnswer = int(input("Multiply:"))
# sets conditions for if user answers question correctly
        if userAnswer == num1*num2:
            counter = counter + 1
# increases score if question is answered correctly
            score = score + 10
            print("Score:", score)
# if 3 or more questions are answered correctly user moves on to next round
            if counter >= 3:
                if score > 200:
                    print("Congrats! You have won the game. Press 2 to play again.")
                    game(userStart)
                else:
                    # prints new score after each question
                    print(
                        "Moving onto the next round! Your score after this round is", score)
                    addition(score)
# creates else statement to set conditions for if user answers question incorrectly
        else:
            print("Incorrect")
# takes away points if user answers question incorrectly
            score = score - 5
            print("Score:", score)

# create function and set parameters for squared operator


def squared(score):
    # sets counter for squared round
    counter = 0
# creates while loop for iteration until program is terminated once conditions are met
    while counter < 3:
        # generate random numbers
        num1 = random.randrange(1, 10)
        num2 = 2
# print randomly chosen number to be squared
        print("Square:", num1)
# user inputs answer to problem
        userAnswer = int(input("Your answer:"))
# sets conditions for if user answers question correctly
        if userAnswer == pow(num1, num2):
            counter = counter + 1
# increases score if question is answered correctly
            score = score + 20
            print("Score:", score)
# if 3 or more questions are answered correctly user moves on to next round
        if counter >= 3:
            if score > 200:
                print("Congrats! You have won the game. Press 2 to play again.")
                game(userStart)
                # if 3 or more questions are answered correctly user moves on to next round
            else:  # and then also come down where im highlighted
                print(
                    "Moving onto the next round! Your score after this round is", score)
                cubed(score)
# creates else statement to set conditions for if user answers question incorrectly
    else:
        print("Incorrect")
# takes away points if user answers question incorrectly
        score = score - 5
        print("Score:", score)

# create function and set parameters for cubed operator


def cubed(score):
    # sets counter for squared round
    counter = 0
# creates while loop for iteration until program is terminated once conditions are met
    while counter < 3:
        # generate random numbers
        num1 = random.randrange(1, 6)
        num2 = 3
# print randomly chosen number to be squared
        print("Cube:", num1)
# user inputs answer to problem
        userAnswer = int(input("Your answer:"))
# sets conditions for if user answers question correctly
        if userAnswer == num1**num2:
            counter = counter + 1
# increases score if question is answered correctly
            score = score + 20
            print("Score:", score)
            if score > 200:
                print("Congrats,")
# if 3 or more questions are answered correctly user moves on to next round
            if counter >= 3:
                if score > 200:
                    print("Congrats,")
                else:
                    # prints new score after each question
                    print(
                        "Moving onto the next round!! Your score after this round is", score)
                    multi(score)
# creates else statement to set conditions for if user answers question incorrectly
        else:
            print("Incorrect")
# takes away points if user answers question incorrectly
            score = score - 5
            print("Score:", score)

# create function and set parameters for start of the game


def game(userStart):
    while userStart > 2:
        # if user selects number greater than 2 ask to choose a number again
        if userStart > 2:
            userStart = int(
                input("Please choose only numbers 1 or 2 to proceed!"))
# if user selects 1 relay instructions to game
    else:
        # instructions for the game
        if userStart == 1:
            print("Step 1 - Press 2 to begin the game!")
            print(
                "Step 2 - Solve given problems (addition, subtraction, multiplication, squaring numbers, cubing numbers")
            print("Step 3 - You will move onto the next round or next operation when you solve 3 questions from the previous round correctly")
            print("Step 4 - Your points will increase as you get questions right and decrease as you get questions wrong")
            print(
                "Step 5 - You have won the game if you have reached 200 points or more!")
            userStart = int(input("Click 2 to start the game"))
# if user selects 2 the game starts
        if userStart == 2:
            # define mathematical operators
            multiply = ("Multiply the numbers.")
            add = ("Add the numbers ")
            sub = ("Subtract the numbers.")
            square = ("Square the number.")
            cube = ("Cube the number.")
# create list to store mathematical operations
            mathops = [multiply, add, sub, square, cube]
# randomly chooses a mathematical operator
            randomops = random.randrange(0, 4)
            x = print(mathops[randomops])
            if randomops == 0:
                multi(score)
            if randomops == 1:
                addition(score)
            if randomops == 2:
                subtraction(score)
            if randomops == 3:
                squared(score)
            if randomops == 4:
                cubed(score)


# calls start of game
game(userStart)
