import random
import function_lib as function_lib
import superbowllistbobby as funny
def normal_play()
    if line_of_scrim > 25:
        user_input = int(input("Choose a play coach! 1.Pass 2.Run: "))
        function_lib.star_line()
        return 
line_of_scrim = 50
distance = line_of_scrim - line_of_scrim
clock = 120
qb_random = random.randint(0, 4)
funny_random = random.randint(0, 2)
random_num_pass = random.randint(0, 5)
random_num_run = random.randint(8, 10)
current_down = 1
total_yards = 0
double_pass = 0
double_run = 0
double_run_fumble = 0
random_num_kick = random.randint(0, 1)
qb_calls =  ["Quarterback audibles at the the line: 'blue 80 on three, blue 80… blue 80… hut hut hut.'", "Quarterback barks: 'Red 80! Red 80! Hut! Hut! Hut!'", "Quarterback: 'Green 18...Green 18….. set-hut!'", "Quarterback: play call '319…319… hut!'", "Quarterback: Ready…..  set hut!"]
nfl_teams = ["Falcons", "Bills", "Packers", "Chiefs",
             "Steelers", "Saints", "Giants", "Eagles", "49ers"]

function_lib.blank_line()
print("WELCOME TO THE NFL SUPERBOWL TERMINAL GAME")
function_lib.blank_line()
function_lib.star_line()
your_team = (input(f"Pick a team from the list {nfl_teams} : ")).title()
function_lib.star_line()
print(f"""
Over the past twenty years the New England Patriots have dominated the NFL 
landscape by participating in 9 Super Bowls and winning six. Every new season 
teams try to emulate them by getting players to take less money while building 
a talented roster to have a chance at winning the Super Bowl. This year the {your_team} 
have succeeded at making the Super Bowl and is 1:00 minute away from dethroning the mighty 
New England Patriots and winning a Super Bowl. Down by two points the odds 
are currently stacked against the {your_team} with the ball at the 50 yard line. 
You have to drive the ball down field and score to win the game. Should you succeed the {your_team} 
will become Super Bowl Champions.
""")
function_lib.star_line()
function_lib.blank_line()
function_lib.rules()
print("If you reach the 0 yard line,", your_team, "wins the game, else the", your_team, "lose.")
function_lib.blank_line()
function_lib.star_line()
function_lib.blank_line()
print(your_team, "are at the", line_of_scrim, "Yard Line")


while line_of_scrim > 0:
    function_lib.blank_line()
    move_clock = 0
    function_lib.star_line()

    if line_of_scrim > 25:
        user_input = int(input("Choose a play coach! 1.Pass 2.Run: "))
        function_lib.star_line()

    if line_of_scrim < 25: 
        user_input = int(input("Choose a play coach! 1.Pass 2.Run 3.Kick: "))
        function_lib.star_line()

    if user_input == 1:
        line_of_scrim -= random_num_pass
        move_clock = abs(random_num_pass) + 10
        function_lib.blank_line()
        print(qb_calls[qb_random])
        function_lib.blank_line() 
        print("Quarter Back passed the football")
        if random_num_pass > 0:
            print("Pass complete:", your_team, "gained", random_num_pass, "yards.")
        if random_num_pass == 0:
            print("Incomplete pass.")
        if random_num_pass < 0:
            print("Quarter Back was sacked")
            print("and loss", abs(random_num_pass), "yards.")
            print(funny.qb_sack[funny_random])

    if user_input == 2:
        line_of_scrim -= random_num_run
        move_clock = random_num_run + 4
        function_lib.blank_line()
        print(qb_calls[qb_random])
        function_lib.blank_line()
        print("Running back ran the football")
        if random_num_run > 0:
            print("and ran for", random_num_run, "yards.")
        if random_num_run == 0:
            print("No gain.")
        if random_num_run < 0:
            print("and was tackled behind the line")
            print("and loss", abs(random_num_run), "yards.")
 
    if line_of_scrim < 15:
        random_num_kick = 1
    
    elif line_of_scrim > 15:
        random_num_kick = random.randint(0, 1)
 
    if user_input == 3:

        function_lib.blank_line()
        print("Kicker kicked the football")
        if random_num_kick == 0:
            print("and scored,", your_team, "win!")
            function_lib.status(1)
            break
        if random_num_kick == 1:
            print("and missed,", your_team, "lose.")
            function_lib.status(2)
            break

    qb_random = random.randint(0, 4)
    clock -= move_clock

    if user_input == 2:
        total_yards = total_yards + random_num_run
    elif user_input == 1:
        total_yards = total_yards + random_num_pass

    double_pass += 1

    if double_pass == 2:
        # random.randint(-5, 1)
        random_num_pass = random.randint(-5, 1)
        double_pass = 0

    else:
        # random.randint(5, 2)
        random_num_pass = random.randint(5, 25) 

    if user_input == 2:
        double_run_fumble += 1

    double_run += 1
    
    if user_input == 2:
        if double_run_fumble == 4:
            print("Fumble, game over.", your_team, "lose.")
            function_lib.status(2)
            break

    if line_of_scrim > 20:

        if double_run == 3:
            # random.randint(-3, 0)
            random_num_run = random.randint(-3, 0)
            double_run = 0

        else:
            # random.randint(-2, 10)
            random_num_run = random.randint(-2, 10) 

    current_down += 1

    if total_yards >= 10:
        current_down = 1

    if line_of_scrim >= 0:
    
        if clock > 0:
            if current_down < 5:           
                function_lib.simple_line()
                function_lib.blank_line()
                if total_yards >= 10:
                    print(funny.first_down[funny_random])
                elif current_down == 2:
                    print(funny.second_down[funny_random])
                elif current_down == 3:
                    print(funny.third_down[funny_random])
                elif current_down == 4:
                    print(funny.fourth_down[funny_random])
                print(your_team,"are at the", line_of_scrim, "Yard Line")
                # print("Current Down:", current_down) 
                print("Game Clock:", clock, "Seconds")

    if total_yards >= 10:
        total_yards = 0    

    if total_yards > 0:
        if clock >= 0:
            if current_down < 5:
                print(your_team, "need", 10 - total_yards, "yards for a first down")

    if total_yards <= 0:
        print(your_team, "need", 10 + abs(total_yards), "yards for a first down")
    
    function_lib.simple_line()
    
    if line_of_scrim <= 0:
        function_lib.blank_line()
        print("Touchdown,", your_team, "win!")
        import winningstars as win
        function_lib.status(1)
        break

    if clock <= 0:
        function_lib.blank_line()
        print("Time Expired.", your_team, "lose.")
        function_lib.status(2)
        break

    if current_down > 4:
        function_lib.blank_line()
        print("No more downs", your_team, "lose.")
        function_lib.status(2)
        break    
