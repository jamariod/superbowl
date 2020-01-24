

import random
line_of_scrim = 50
distance = line_of_scrim - line_of_scrim
clock = 120
random_num_pass = random.randint(0, 10)
random_num_run = random.randint(10, 20)
current_down = 1
total_yards = 0
double_pass = 0
double_run = 0
double_run_fumble = 0

nfl_teams = ["Falcons", "Bills", "Packers", "Chiefs",
             "Steelers", "Saints", "Giants", "Eagles", "49ers"]

your_team = (input(f"Pick a team from the list {nfl_teams} : "))

if your_team in nfl_teams:
    print(f"""
    Over the past twenty years the New England Patriots have dominated the NFL 
    landscape by participating in 9 Super Bowls and winning six. Every new season 
    teams try to emulate them by getting players to take less money while building 
    a talented roster to have a chance at winning the Super Bowl. This years the {your_team} 
    succeeding at making the Super Bowl and is 2:00 minutes away from dethroning the mighty 
    New England Patriots and winning a Super Bowl. Down by two points and unable to kick a 
    field due to the kicker breaking his leg during the first half of the game. The odds 
    are currently stacked against the {your_team} with the ball at your 25 yard line. 
    You have to drive the ball down field 75 yards to win the game.Should you succeed {your_team} 
    will become Super Bowl Champions.
    """)

print("You are at the", line_of_scrim, "Yard Line")

while line_of_scrim > 0:
    print()
    move_clock = 0

    if line_of_scrim > 20:
        user_input = int(
            input("Choose a play coach! 1.Pass 2.Run: "))
        print("*****************************************************")

    if line_of_scrim < 20:
        user_input = int(
            input("Choose a play coach! 1.Pass 2.Run 3.Kick: "))
        print("*****************************************************")

    if user_input == 1:
        line_of_scrim -= random_num_pass
        move_clock = abs(random_num_pass) + 10

        print()
        print(f"{your_team} quarter back passed the football")
        if random_num_pass > 0:
            print("Pass complete: User gained", random_num_pass, "yards.")
        if random_num_pass == 0:
            print("Incomplete pass.")
        if random_num_pass < 0:
            print(f"{your_team} quarter back was sacked")
            print("and loss", abs(random_num_pass), "yards.")

    if user_input == 2:
        line_of_scrim -= random_num_run
        move_clock = random_num_run + 4

        print()
        print(f"{your_team} unning back ran the football")
        if random_num_run > 0:
            print("and Ran for", random_num_run, "yards.")
        if random_num_run == 0:
            print("No gain.")
        if random_num_run < 0:
            print("and was tackled behind the line")
            print("and loss", abs(random_num_run), "yards.")

    if user_input == 3:

        print()
        print(f"{your_team} kicker kicked the football")
        if random_num_kick == 0:
            print("and scored, You win!")
            break
        if random_num_kick == 1:
            print("and missed, You lose.")
            break

    clock -= move_clock

    if user_input == 2:
        total_yards = total_yards + random_num_run
    if user_input == 1:
        total_yards = total_yards + random_num_pass

    double_pass += 1

    if double_pass == 2:
        random.randint(-20, 0)
        random_num_pass = random.randint(-20, 0)
        double_pass = 0

    else:
        random.randint(-10, 2)
        random_num_pass = random.randint(-10, 25)

    double_run_fumble += 1
    double_run += 1

    if user_input == 2:
        if double_run_fumble == 4:
            print(f"{your_team} fumble, game over.")
            break

    if double_run == 2:
        random.randint(-3, 0)
        random_num_run = random.randint(-3, 0)
        double_run = 0

    else:
        random.randint(-2, 10)
        random_num_run = random.randint(-2, 10)

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
