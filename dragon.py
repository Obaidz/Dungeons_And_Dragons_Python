from random import randint
from sys import exit
import random
secure_random = random.SystemRandom()         # Declaring random fuction to one variable that can br used later.
dungeon = []

class character(object):
    def __init__(self, name, health, attack, defence, items):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.items = items

class Enemy(object):
    def __init__(self, ename, ehealth, eattack, edefence):
        self.ename = ename
        self.ehealth = ehealth
        self.eattack = eattack
        self.edefence = edefence
        
class item(object):
    def __init__(self, helmet, armour, stick, sword, potion, seed, score):
        self.helmet = helmet
        self.armour = armour
        self.stick = stick
        self.sword = sword
        self.potion = potion
        self.seed = seed
        self.score = score
 
        
        
   

    
def game(dung):
    
    PH = randint(130, 350)                          #Giving random values to the player.
    PA = randint(80, 150)
    PD = randint(80, 150)
    PI = 0
    name = str(raw_input("Type you Name please: "))     

    player = character(name, PH, PA, PD, PI )     # Using object for player 

    


    


    Type = str(raw_input("Enter Game level, E for easy, M for medium & D for difficult: "))    # For Game difficulty. length of list
    
    if Type == "E":                                            #   dung = dungeon,
        dung = [z * 0 for z in range(randint(3, 6))]     
        print dung

    elif Type == "M":
        dung = [z * 0 for z in range(randint(7, 11))]
        print dung

    elif Type == "D":
        dung = [z * 0 for z in range(randint(12, 20))]
        print dung

    else:
        print "Wrong input, try again"
        game(dungeon)

    try:
        name = player.name              # Giving object values to variables for players.
        Phealth = player.health
        Pattack = player.attack
        Pdefence = player.defence
        Pitems = player.items
        

        
    
    except:
        print "This is an error in Game Method at start"


   
    
    
   
   
    PlayerValues = [Phealth, Pitems, 0]           # For storing player health, items and score.  
    for i in range(0, len(dung)):           # Dungeon list with items treated as Rooms.
        
        Enemies = randint(1, 5)
        score = PlayerValues[2]

        if i >= 0:
            print
                
            print   """            ###############
            ## NEXT ROOM ##
            ##  ROOM NO  ##
            ##      %d    ##
            ###############"""% (i+1)

        while Enemies > 0:      # Each Room filled with enemies.

            FL = ["A", "C", "F", "E", "G"]      #  Random Name generator for Enemeies.
            SL = ["l", "y"]
            TL = "a"
            fL = "n"                            #
     
            EN = str(secure_random.choice(FL)) + str(secure_random.choice(SL)) + TL + fL
            EH = randint(50, 80)
            EA = randint(30, 40)
            ED = randint(30, 40)

            EnemyChar = Enemy(EN, EH, EA, ED)

            Ename = EnemyChar.ename
            Ehealth = EnemyChar.ehealth
            Eattack = EnemyChar.eattack
            Edefence = EnemyChar.edefence
            
            
            Phealth = PlayerValues[0]
            Pitems = PlayerValues[1]
            print
            print """            player_name: %s
            player_health: %d
            player_attack: %d
            player_defence: %d
            player_items: %d
            """% (name, Phealth, Pattack, Pdefence, Pitems)

            print
            print "Enemy Info"
            print """            Enemy_name: %s
            Enemy_health: %d
            Enemy_attack: %d
            Enemy_defence: %d
            """% (Ename, Ehealth, Eattack, Edefence)
            print "Total Number of Rooms are: %d"% (len(dung))
            
            print "Total number of enemies left in room %d are: %d " % ((i + 1), Enemies)

            while Phealth > 0 or Ehealth > 0:
                s = str(raw_input("Press Enter Key to play the game and Q to quit please! "))
                if s == "":
                    PAtck = randint(30, PA)
                    EAtck = randint(20, EA)
                    PDfnce = randint(30, PD)
                    EDfnce = randint(20, ED)

                    if PAtck > EDfnce:
                        print "%s hit %s"% (name, Ename)
                        damage = PAtck - EDfnce
                        score = damage
                        print "damaged done: %d, score gain: %d"%  (damage, score)
                        PlayerValues[2] += score
                        Ehealth -= damage
                        print "%s health left: %d"% (Ename, Ehealth)
                        print
                        

                    else:
                        print "%s Attack missed "% name
                        
                        print 

                    if EAtck > PDfnce:
                        print "%s hit %s"% (Ename, name)
                        damage = EAtck - PDfnce
                        Phealth -= damage
                        print "damaged done: %d, %s health: %d"% (damage, name, Phealth)
                        print
                       

                    else:
                        print "%s Attack missed"% Ename
                       
                        print

                    print "Total Score of %s is: %d"% (name, PlayerValues[2])
                    
                    print
                    print

                    Randompickups = randint(1, 58)
                    Playeritems = item(10, 40, 10, 40, 10, 40, PlayerValues[2])

                    if  Phealth <= 0:
                        print "%s has lost the game against the goblin %s. GAMEOVER"% (name, Ename)
                        print "Total %s's score: %d"% (name, PlayerValues[2])
                        print
                        exit(0)

                    elif Ehealth <= 0:
                        print "%s loses, %s Wins, with current score in this room: %d."% (Ename, name, PlayerValues[2])
                        print "                 ________________________"
                        print
                        helmet = Playeritems.helmet
                        armour = Playeritems.armour
                        stick = Playeritems.stick
                        sword = Playeritems.sword
                        potion = Playeritems.potion
                        seed = Playeritems.seed
                        healthpickups = 0
                        defencepickups = 0
                        attackpickups = 0
                        
                        if PlayerValues[1] < 3:
                            if Randompickups > 0 and Randompickups < 16:
                                print "you gained health potion as a Bonus."
                                print "previous health value: %d."% (Phealth)
                                Phealth += potion
                                print " New health value: %d"% (Phealth)
                                print
                                

                            if Randompickups > 15 and Randompickups < 19:
                                if healthpickups >= 1:
                                    print "You already have this Health item. i.e Seed."
                                    

                                else:
                                    print "you gained health Seed."
                                    print "previous health value: %d."% (Phealth)
                                    Phealth += seed
                                    print " New health value: %d"% (Phealth)
                                    
                                    healthpickups += 1
                                    print

                            if Randompickups > 18 and Randompickups < 24:
                                if attackpickups >= 1:
                                    print "You already have this attack item. i.e stick."
                                    

                                else:
                                    print "you gained stick for attack."
                                    print "previous attack value: %d."% (PA)
                                    PA += stick
                                    print "New attack value: %d"% (PA)
                                    
                                    attackpickups += 1
                                    print

                            if Randompickups > 23 and Randompickups < 29:
                                if attackpickups >= 1:
                                    PA -= stick    # Dropping stick to gain sword.
                                    print "Dropping stick to gain sword."
                                    PA += sword
                                    print "New attack value: %d"% (PA)
                                    

                                else:
                                    print "Sword gained."
                                    print "previous attack value: %d."% (PA)
                                    PA += sword
                                    print " New attack value: %d"% (PA)
                                    
                                    attackpickups += 1
                                    print



                            if Randompickups > 28 and Randompickups < 37:
                                if defencepickups >= 1:
                                    print "You already have this defence item. i.e tin helmet."
                                    

                                else:
                                    print "you gained helmet for defence."
                                    print "previous defence value: %d."% (PD)
                                    PD += helmet
                                    print " New defence value: %d"% (PD)
                                    
                                    defencepickups += 1
                                    print

                            if Randompickups > 36 and Randompickups < 43:
                                if defencepickups >= 1:
                                    PD -= helmet    # Dropping stick to gain sword.
                                    print "Dropping helmet to gain armour."
                                    PD += armour
                                    print "New defence value: %d"% (PD)
                                    

                                else:
                                    print "Armour gained."
                                    print "previous defence value: %d."% (PD)
                                    PD += armour
                                    print " New defence value: %d"% (PD)
                                    
                                    defencepickups += 1
                                    print

                            if Randompickups > 42 and Randompickups < 59:
                                print "You gained no items."
                                

                            PlayerValues[1] += healthpickups + defencepickups + attackpickups
                            print "Total items gained: %d "% (PlayerValues[1])

                        elif PlayerValues[1] >= 3 and Enemies > 0:
                            print "You already have three items."
                        
                        break






                            
                elif s == "Q":
                    print
                    print "Quitting..."
                    
                    print
                    exit(0)
                else:
                    print "Wrong option, please press ENTER key"

                PlayerValues[0] = Phealth
                PlayerValues[1] = Pitems
                
            
            Enemies -= 1
        
        if ( i == (len(dung) - 1) and Enemies <= 0):
            print
            print
            print "Player %s Won the Game"% (name)
           
            print "Bye......" 
           
            print
            print
            exit(0)

      


            





def main():

    game(dungeon)
    
main()
                


        