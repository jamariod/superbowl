#This file will be updated with classes once we get it fully functional.

#this imports the random library into the file.
import random

#this creates the stick_position's value to start the game (50 yard line).
stick_position = 50

#We will use these variables in the future. Not sure how so they may get scratched.
stick_position2 = 50
distance = stick_position - stick_position

#this is the clock variable, we will subtract time from the clock after each play.
clock = 120

#this creates the variable that will hold the random number generated from a passing play.
random_num_pass = random.randint(0, 10)

#the creates the variable that will hold the random number generated from a running play.
random_num_run = random.randint(10, 20)

#this is the current down variable.
current_down = 1

#before the loop starts this lets the player know where they are on the field.
#it reads the stick_position variable and returns the number into the print statement.
print("You are at the", stick_position, "Yard Line")

#this while loop starts the game
# as long as the sitck_position is less than 100 (the opponents end zone) the loop will keep running.
#____________________________________________________________________________________________________
while stick_position > 0:
    print()
    move_clock = 0
#this requires a input from the user to choose a play.
    user_input = int(input("Choose a play coach! 1.Pass 2.Run: "))

#(PASS PLAY) if the user inputs 1 (pass) the statement will subtract the random number of yards gained from the stick position 
#getting the user closer to the goal line.
    if user_input == 1:
        stick_position -= random_num_pass
        move_clock = random_num_pass + 10
        print()
        print("User passed the football")
        if random_num_pass > 0:
            print("Pass complete: User gained", random_num_pass, "yards.")
        if random_num_pass == 0:
            print("Incomplete pass.")
        if random_num_pass < 0:
            print("User was sacked")

#(RUN PLAY) if the user inputs 2 (run) the statement will subtract the random number of yards gained from the stick position 
#getting the user closer to the goal line.
    if user_input == 2:
        stick_position -= abs(random_num_run)
        move_clock = random_num_run * 4
        print()
        print("User ran the football")

#____________________________________________________________________________________________________
#needs and else statement to catch all invalid inputs from the user.

#moves to next down after the play is run.    
    current_down += 1
    clock -= move_clock
    random_num_pass = random.randint(-5, 10)
    random_num_run = random.randint(10, 20)

#keeps printing current down if user hasn't reached the goal line.
    if stick_position > 0:
        print("Current Down:", current_down) 
        print("User is at the", stick_position, "Yard Line")
        if clock > 0:
            print("Game Clock:", clock, "Seconds")

    if clock <= 0:
        print("Time Expired. You Lose.")
        break

#resets the current down to 0 after running the 4th down play.
    if current_down == 4:
        current_down = 0    

#prints touchdown and breaks the loop if the stick_position is over the end zone (0).
    if stick_position <= 0:
        print("Touchdown, you won!")
        break
