def heart_rate(age, goal):
    max_HR = 220 - age
    print("Your maximum heart rate is:", max_HR)

    if goal == "S":
        lower_target = (max_HR * 0.80)
        higher_target = (max_HR * 1)
        print("Your target heart rate is between", lower_target, "and", higher_target)
    else:
        lower_target = (max_HR * 0.60)
        higher_target = (max_HR * 0.80)
        print("Your target heart rate is between", lower_target, "and", higher_target)
    

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")
heart_rate(user_age, user_goal)
