def status(outcome):  
    if outcome == 1:
        print("************************************")
        print("    *     *   ******    *    *    ")
        print("     *   *    *    *    *    *    ")
        print("       *      *    *    *    *    ")     
        print("       *      ******    ******    ")
        print()
        print(" *     *     *    *****     **   *")
        print("  *    *    *       *       * *  *")
        print("   *  *  * *        *       *  * *")
        print("    *     *       *****     *   **")
        print("************************************")
        return 

    if outcome == 2:
        print("************************************")
        print("    *     *   ******    *    *")
        print("     *   *    *    *    *    *")
        print("       *      *    *    *    *")     
        print("       *      ******    ******")
        print()
        print(" *        ******    ******   ****** ")
        print(" *        *    *    *        *      ")
        print(" *        *    *    ******   ****** ")        
        print(" *        *    *         *   *      ")
        print(" ******   ******    ******   ****** ")
        print("************************************")
        return 

def star_line():
    print("*****************************************************")
    return 

def simple_line():
    print("_____________________________________________________")
    return 

def rules():
    print("Rules of the game:")
    print()
    print("Passing plays are worth 25 yards maxium, but be careful as over use of the passing play will result in a sack.")
    print("Running plays are worth 10 yards maxium, but be careful as over use of the running play will result in a fumble and you will lose the game.")
    print("If you reach the 20 yard line, you have the option to kick the winning field goal.")
    return 

def blank_line():
    print()
    return 



# nfl_teams = ["Falcons", "Bills", "Packers", "Chiefs", "Steelers", "Saints", "Giants", "Eagles", "49ers"]



# def storyline():
#     your_team = (input(f"Pick a team from the list {nfl_teams} : ")).title()    
#     if your_team in nfl_teams:
#         print("*****************************************************")
#         print(f"""
#         Over the past twenty years the New England Patriots have dominated the NFL 
#         landscape by participating in 9 Super Bowls and winning six. Every new season 
#         teams try to emulate them by getting players to take less money while building 
#         a talented roster to have a chance at winning the Super Bowl. This year the {your_team} 
#         have succeeded at making the Super Bowl and is 1:00 minute away from dethroning the mighty 
#         New England Patriots and winning a Super Bowl. Down by two points the odds 
#         are currently stacked against the {your_team} with the ball at the 50 yard line. 
#         You have to drive the ball down field and score to win the game. Should you succeed {your_team} 
#         will become Super Bowl Champions.
#         """)
 

#print(status(1))
