import random
import math
total_gold=0
total_gold_2=0
#win=math.floor(random.uniform(0,1/(1-chance)))
i=0
def fight(chance):
    #chance=0.80
    win=math.floor(random.uniform(0,1/(1-chance)))
    gold = 0
    if win >= 1:
        gold+=300
        return gold
    else:
        gold=-300
        return gold

testing_chance=input("Please enter the percent chance of win you want to test:")
testing_chance=float(testing_chance)
testing_num=testing_chance/100
testing_chance2=input("Please enter the 2nd percent chance of win you want to test against the first:")
testing_chance2=float(testing_chance2)
testing_num2=testing_chance2/100
for i in range (0,5):
    gold_won=fight(testing_num)
    total_gold+=gold_won
    i=i+1

for i2 in range (0,10):
    gold_won=fight(testing_num2)
    total_gold_2+=gold_won
    i2=i2+1



average_gold=total_gold/i
average_gold_2=total_gold_2/i2
print("After "+str(i)+" fights at a "+str(testing_chance)+"% chance of winning, the average for gold is: "+str(average_gold)+" gold.") 
print("After "+str(i2)+" fights at a "+str(testing_chance2)+"% chance of winning, the average for gold is: "+str(average_gold_2)+" gold.") 
#print(total_gold)
