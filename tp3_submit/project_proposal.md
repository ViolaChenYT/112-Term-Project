Name:Viola Chen Yitao
Andrew ID: yitaoche
------------------------------Dec 04 2019 -----------------------
# user study feedback
The learning curve for the game is a bit too deep ie. many of the controls and keyboard shortcut and mouse-key coordinations are very foreign for people who have never played similar games before.
As a respond to this, I have improved my help screen feature and the instructions and also added a quick notice bar at the bottom of the screen notifying player what can be done with the current unit selected.
______________________________Dec 04 2019 _______________________
# TP3 update

mainly working on minimap, game play improvement such as shortcut to group select / switch camera position, more powerups/bonus features included

-------------------------------------------------------------------------
#Project description:
The preliminary title for this project is 'Immunity War'. This is an interactive game where the player will play the role of immune system to defend the invasion of viruses (into the body), with real-time-strategy style. ie. control units to move around and attack, construct buildings and farm resources.
The goal of the immune system is to eliminate a given number of viruses (the level of difficulty could increase with increasing number of viruses being killed), whereaas the goal of the viruses is to destroy all the buildings of the immune system.

#Competitive analysis:
This project aims to learn from well-made real-time-strategy games such as StarCraft2 or WarCraft3.This project would be similar to those mentioned above in terms of the general game set-up and basic game-play such as movements, constructions, grouping of units and even key-binding.
However, this project would be different from those mentioned above in terms of winning/losing conditions and the significantly different goals of the 2 parties in opposition.

#Structural plan:
The final project will have 4 files. 1 is the main file that contains the game loop and all the events functions. The second file would be one that contains the class player and all its relevant informations, such as cells of the immune system, the buildings that have been built. The third file will contain all the information about the attacker, including the class viruses and all its methods, the intended simple game AI would also be in this file. The last file would be the terrain ie. map that the game would take place in, and its relevant constraints. 

#Algorithmic plan:
I think there are 2 parts that are algorithmically challenging. 
1) a playable game AI and its decision making. I plan to adapt from the minimax algorithm but individual and collective decision making can be tricky.
2) terrain generation to make sure there is a way to reach all places and hopefully no dead end either.This will probably be done with some sort of backtracking.

#Timeline plan:
Week 1: basic class structures
Week 2: playable AI, terrain generation
Week 3: graphics, user interface improvement

#Version control plan:
I back up my code daily onto my private github repository. Different versions are named differently as tpx.y_filename.py, where x is the week and y is the different versions, aided by each commit message.

#Module list:
pygame

#TP2 Update
-github url:
 https://github.com/FatRabbitTao/112-Term-Project.git
-algorithm design change:
 new source of complexity: collision system and prevention of all collisions
 			farming system - minions moving back and forth in loops automatically
-time line change:
	terrain generation and graphics in tp3, focus on advanced game play in week 2
-multiplayer version may not be implemented


