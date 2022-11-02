import random
from random import randint

class hero:
    def __init__(self,name,level,exp,expToLevel,heroAttack,heroHP,newAcc):
        self.name = name
        self.level = level
        self.exp = exp
        self.expToLevel = expToLevel
        self.heroAttack = heroAttack   
        self.heroHP = heroHP
        self.newAcc = newAcc

    def __str__(self):
        return f"Welcome {heroName}!"
        



class monEncounter:
    def __init__(self,creatureType,creatureLevel,creatureExpValue,monAttack,monHP):
        self.creatureType = creatureType
        self.creatureLevel = creatureLevel
        self.creatureExpValue = creatureExpValue
        self.monAttack = monAttack
        self.monHP = monHP

    def __str__(self):
        return f"A level {creatureLvl} {monster} attacks! The {monster} has {creatureAttack} attack and {creatureHealth} health!"
def attacked():
    monList = ['zombie','skeleton','necromancer']
    monster = random.choice(monList)
    creatureLvl = randint(1,3)
    if monster == "skeleton":
        creatureHealth = creatureLvl * 2
        creatureAttack = creatureLvl * 4
        creatureExp = creatureHealth * 3
        return monster, creatureLvl, creatureExp, creatureAttack, creatureHealth
        
    elif monster == "zombie":
        creatureHealth = creatureLvl * 4
        creatureAttack = creatureLvl * 2
        creatureExp = creatureHealth * 3
        return monster, creatureLvl, creatureExp, creatureAttack, creatureHealth
    elif monster == "necromancer":
        creatureHealth = creatureLvl * 4
        creatureAttack = creatureLvl * 4
        creatureExp = creatureHealth * 4
        return monster, creatureLvl, creatureExp, creatureAttack, creatureHealth

    else:
        print("error")
attack=0
not_attack = 0
#for i in range(1,5):
#    travel = randint(0,1)
#    if travel == 0:
#        monster, creatureLvl, creatureExp, creatureAttack, creatureHealth = attacked()
#        new_mon = monEncounter(monster,creatureLvl,creatureExp,creatureAttack, creatureHealth)
#        attack+=1
#        print(new_mon)
#    elif travel == 1:
#        not_attack+=1
#        print("You push forward into the night.")
#    i+=1



#print("Not Attacked: %d"%not_attack)
#print("Attacked: %d"%attack)
heroName = input('Greetings! Enter the name you wish your character to be: ')
ans = input('You entered: '+heroName+'. Do you wish to continue with this name? (Type yes/no)')
if ans == 'yes' or ans == 'Yes':
    new_hero = hero(heroName,1,0,14,2,10,'yes')
    print(new_hero)
elif ans == 'no' or ans == 'No':
    ans2=input('Would you like to enter a different name? (Type yes/no)')
    if ans2 == 'Yes' or ans2 == 'yes':
        heroName = input('Enter the name you wish to go by: ')
        new_hero = hero(heroName,1,0,14,2,10,'yes')
        print(new_hero)
    else:
        print('Fair enough! Goodbye!')
else:
    print('error')

travelYesorNo = input("Would you like to try traveling? (Type yes/no)")
if travelYesorNo == 'yes' or travelYesorNo == 'Yes':
    travel = randint(0,1)
    if travel == 0:
        monster, creatureLvl, creatureExp, creatureAttack, creatureHealth = attacked()
        new_mon = monEncounter(monster,creatureLvl,creatureExp,creatureAttack, creatureHealth)
        attack+=1
        print(new_mon)    
    elif travel == 1:
        not_attack+=1
        print("You push forward into the night.")
elif travelYesorNo == 'No' or travelYesorNo == 'no':
    print("You stay put for the night. The inn is cozy!")
else:
    print("Please enter yes or no")
