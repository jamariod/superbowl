import random
stickpos = 50
stickpos2 = 50
distance = stickpos - stickpos
clock = 120
random_num_run = random.randint(10, 20)
random_num_pass = random.randint(0, 10)
current_down = 1


print("You are at the", stickpos, "Yard Line")
while stickpos < 100:
    if stickpos <= 0:
        print("Touchdown, you won!")
        break
    user_input = int(input("Choose a play. 1. Pass 2. Run: "))
    if user_input == 1:
        stickpos -= random_num_pass
    if user_input == 2:
        stickpos -= random_num_run
    # else:
    #     print("Invalid Input")
    # if random_num_pass >= 10:
  
    if distance >= 10:
      current_down = 1        
    current_down += 1
    if stickpos > 0:
        print("Current down:", current_down, "| You are at the", stickpos, "Yard Line")
    if current_down == 4:
        current_down = 0