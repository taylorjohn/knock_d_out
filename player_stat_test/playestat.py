player = {}
player["wins"] = 0
player["losses"] = 0
player["ranked"] = 13
player["stars"] = 0
player["hearts"] = 0
player["stamina"] = 100
player["points"] = 0
player["current_round"] = 1
player["current_opponent"] = 1


player = {
		  "wins": 0, "losses": 0,
		  "ranked": 13, "stars": 0, "hearts":  0,
		  "stamina": 100, "points": 0, "current_round": 1,
		  "current_opponent": 1
		  }

# Convert to list of tuples.
playerItems = player.items()

# Loop and display tuple items.
for playerItem in playerItems:
    print("Wins:", playerItem[0])
    print("Losses: ", playerItem[1])
    print("Ranked: ", playerItem[2])
    print("Stars", playerItem[3])
    print("Hearts:", playerItem[4])
    print("Stamina: ", playerItem[5])
    print("Points: ", playerItem[6])
    print("Round: ", playerItem[7])
    print("Opponent: ", playerItem[8])
    print("")


print(player)