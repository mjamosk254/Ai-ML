import random #it allows us to generate random numbers and choices

#create a list of actions that ai can choose in the game
actions=["Attack", "Defend", "Heal"]

#score total rewardscollected for each action
total_reward={"Attack":0, "Defend":0,"Heal":0}

#store how many times each action has been used
count={"Attack":0,"Defend":0,"Heal":0}

#The game system - create a function that gives diff rewards depending on the actions choosen
def game_reward(action):
    #if the ai chooses attack
    if action=="Attack":
        return random.randint(5,10)
    #if the ai chooses defend
    elif action=="Defend":
        return random.randint(2,6)
    #if the ai chooses heal
    else:
        return random.randint(4,8)

#Training phase(Exploration)
#Repeat the learning process 100 times
for i in range(100):
    #ai randomly selects an action
    action=random.choice(actions)

    #Get reward based on action
    Reward=game_reward(action)

    #add reward t total score of that action
    total_reward[action] += Reward

    #Increase count  of many times an action was chosen
    count[action] +=1

#calculation phase(learning output)
#Create an empty dict to store avg
avg={}
#loop through eachaction to calculate its average reward
for a in actions:
    avg[a]=total_reward[a] / count[a]

#Results
print("learning results:\n")

#print the avg reward for each action
for a in avg:
    print(a, ":", round(avg[a],2))

#print the best action(highest avg reward)
print("\nBest action:",max(avg, key=avg.get))


