KNOCK'D OUT!!!
======

Simple punch out like game made in pygame.


Still planning out the game

Splash Screen
------

The splash screen has two options to choose between 
  New
  Continue
  
New starts new game from level 1

Continue lets you start off at the last boss you where at with same statistics 

Pre Fight Screen
------

Circuit Name
	Minor Circuit

Players Statistics

FROM LOCATION  (Place of orgin)
AGE:  13      (age in years)
WEIGHT: 107  (weight in pounds)
0 Wins - 0 Losses    0 KOs (Players match record)
RANKED: 13 (Players rank)
PLAYER's NAME (Player's name)

VS.

Opponent's Statistics

FROM LOCATION  (Place of orgin)
AGE:  13      (age in years)
WEIGHT: 107  (weight in pounds)
0 Wins - 0 Losses    0 KOs (Opponents match record)
RANKED: 13 (Opponent's rank)
Opponent's NAME


Screen Displayed Between Rounds
------

These dialogue maybe a helpful hint to winning the match!!

Removes location information
Add The Coaches dialogue of encouragement

ex.  "Stick And Move, Stick And MOVE!"

Opponent's dialogue

ex. "Watch The JAW!! Don't Hit My Jaw!!

During Match Statistics on Screen
------

Hearts
(Number of Hearts)

Hearts (are the Players Fighting spirit)
The Player can punch whenever he has one or more hearts.

He will lose a heart each time his opponent blocks or dodges out of the way of his punches.

If he is hit he loses three hearts.

When the player is to tired to punch (he will change to color (different greenish sprite set) and
must avoi punches by dodging or ducking to gain hearts.


Stars = []
(Number of Stars)
The number of stars controls the number of uppercuts the player can use.

When the player scores an effective punch, 
A star will appear on his head and 
The number of stars will increase by one.

when the player is hit he loses one star 
if knocked down he loses all of his stars.

The Maximum number of stars is three.

Stamina Meters
These meters show how much stima the player and his opponent have left.

Stamina will drop when a boxer is punched.

A boxer will go down if his stamina drops to zero

His stamina will recover when he gets back up (depending on ow quickly he gets back up)

During between splash screen hold down space bar to get additional stamina from coach

Match Points
Match points are won when Player punches his opponent, 
Uppercuts, and effective punches win the greatest number of match points.

Elapsed Time
Show the lapsed time for the current round

Round:
Shows the current round number

Player Moves In GAME
------

K_LEFT
⋅⋅* Dodge to left

K_RIGHT
⋅⋅* Dodge to right

K_Down
⋅⋅* Once: Block
⋅⋅* Twice rapidly ducking

K_SPACE
⋅⋅* If pressed between rounds, Coach's encouraging advice can increase Player's stamina

K_W
⋅⋅* Uppercut (if the number of stars is 1 or greater!)

K_A
⋅⋅* Left body blow
⋅⋅* (when Player is knocked down pressing rapidly and he'll get up)

K_UP & K_A
⋅⋅* pressing up and left punch punch to the left face

K_D
⋅⋅* Left body blow

K_UP & K_D
⋅⋅* pressing up and right punch punch to the left face

Time Events
------

Round
------a round counts up to 3 minutes

KO
⋅⋅*knockout (KO) is when a boxer stays down for a count of 10
⋅⋅*if the player runs out of health he stays down for the count of ten

KO Recovery
⋅⋅*KO Recovery how quickly the player gets back up will determin health If the player recovers at a slow and 
⋅⋅*steady pace, usually ending at the count of 4 #  or 5, they will regain much more health than 
⋅⋅* if they mashed the buttons or waited until the count of 9

TKO
⋅⋅* TKO'd after 3 or 4 total knock downs
⋅⋅* if the player has 3 ko's then they are tko'd and game over

List of Opponents
------


Opponent#1
[Picture] Opponents Nickname
Opponents Name

France's Glass Jaw
GLASS JOE

Ranking: Minor circuit, 2nd
Record: 1 win, 99 losses, 1 KO
Place of Orgin: Paris, France
Age: 38
Weight: 110lbs

Opponent#2
[Picture] Opponents Nickname
Opponents Name

The German Steel Machine
Von Kaiser

Ranking: Minor circuit, top
Record: 23 wins, 13 losses, 10 KO's
Place of Orgin: Berlin, West Germany
Age: 42
Weight: 144lbs

Game Play Tips
------

Basic Boxing Technique

1. More of your punches will reach the opponent if you aim where he's not guarding.

2. Player won't be able to punch when he's tired (when he has no heart's), and his oppent will immediately start punching.

Dodge his punches and recover hearts

3. Player left punch is a little faster than his right, but it's not quite as strong.


Winning Boxing Technique

1. Dodge opponent's punches and then punch back immediately. You'll starle your opponent (his face will show it).

This is your chance --- punch furiously and you should score.

2. If your opponent comes up on the count of 1 after you've knocked hm down, go with a uppercut for a sure knock-down.

3. During an interval: Use the advice of the trainer/coach to your best advantage.


Player Information
------

The Player needs to store the following information and also save and reload a saved game.

I am going to create a dictionary and use repr()/eval() to convert to string and from string:
'''python
data = {
    "PLAYER":Lil Mac,
    "LOCATION": Bronx, NY
    "AGE": 13
    "WEIGHT": 107
    "WINS": 0
    "LOSSES": 0
    "KOs": 0
    "RANKED": 13
    "HEARTS": 0
    "STARS": 0
    "STAMINA": 100
}

with open("data1.txt", "w", encoding="utf-8") as file:
   file.write(repr(data))
file.close()
'''

Then to load:

'''python
with open("data1.txt", "r", encoding="utf-8") as file:
   data_string = file.readline()
   data = eval(data_string)
   print data["PLAYER"]
file.close()
'''
