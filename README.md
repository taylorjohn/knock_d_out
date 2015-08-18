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

