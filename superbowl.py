import random
line_of_scrim = 50
distance = line_of_scrim - line_of_scrim
clock = 60
random_num_pass = random.randint(0, 10)
random_num_run = random.randint(10, 20)
current_down = 1
total_yards = 0
print("You are at the", line_of_scrim, "Yard Line")

while line_of_scrim > 0:
    print()
    move_clock = 0

    user_input = int(input("Choose a play coach! 1.Pass 2.Run: "))
    print("*****************************************************")

    if user_input == 1:
        line_of_scrim -= random_num_pass
        move_clock = random_num_pass + 10

        print()
        print("Quarter Back passed the football")
        if random_num_pass > 0:
            print("Pass complete: User gained", random_num_pass, "yards.")
        if random_num_pass == 0:
            print("Incomplete pass.")
        if random_num_pass < 0:
            print("Quarter Back was sacked")
            print("and loss", abs(random_num_pass), "yards.")

    if user_input == 2:
        line_of_scrim -= random_num_run
        move_clock = random_num_run + 4

        print()
        print("Running back ran the football")
        if random_num_run > 0:
            print("and Ran for", random_num_run, "yards.")
        if random_num_run == 0:
            print("No gain.")
        if random_num_run < 0:
            print("and was tackled behind the line")
            print("and loss", abs(random_num_run), "yards.")

    clock -= move_clock

    if user_input == 2:
        total_yards = total_yards + random_num_run
    if user_input == 1:
        total_yards = total_yards + random_num_pass

    random_num_pass = random.randint(-10, 25)
    random_num_run = random.randint(-2, 15)

    current_down += 1

    if total_yards >= 10:
        current_down = 1

    if line_of_scrim > 0:
        if clock > 0:
            if current_down < 5:
                print("_____________________________________________________")
                print()
                print("Current Down:", current_down) 
                print("Game Clock:", clock, "Seconds")
                print("User is at the", line_of_scrim, "Yard Line")

    if total_yards >= 10:
        total_yards = 0    

    if total_yards > 0:
        print("You need", 10 - total_yards, "yards for a first down")

    if total_yards <= 0:
        print("You need", 10 + abs(total_yards), "yards for a first down")
    
    print("_____________________________________________________")

    if clock <= 0:
        print()
        print("Time Expired. You Lose.")
        break

    if current_down > 4:
        print()
        print("No more downs. You Lose.")
        break    

    if line_of_scrim <= 0:
        print()
        print("Touchdown, you won!")
        break

print("**********************************************************")