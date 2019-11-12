import numpy as np
import random, time

def roll(cmd):
	global dices
	dice = dices[cmd]
	point = random.choice(dice)
	return point

# dices = np.array([
# 	[3, 3, 3, 3, 3, 3],
# 	[0, 0, 4, 4, 4, 4],
# 	[1, 1, 1, 5, 5, 5],
# 	[2, 2, 2, 2, 6, 6]])

dices = np.array([
	[3, 3, 3, 3],
	[0, 4, 4, 4],
	[1, 1, 5, 5],
	[2, 2, 2, 6]])

your_score = 0
enemy_score = 0
max_score = 100

while max(your_score, enemy_score) < max_score:
	your_dice = int(raw_input("Choose your dice (1-4): ")) - 1
	your_point = roll(your_dice)
	your_score += your_point
	time.sleep(0.125)
	print "You got {}!\tYour score is: {}".format(your_point, your_score)
	
	enemy_dice = (your_dice + 1) % 4
	enemy_point = roll(enemy_dice)
	enemy_score += enemy_point
	time.sleep(0.125)
	print "Enemy got {}!\tEnemy score is: {}\n".format(enemy_point, enemy_score)

if your_score > enemy_score:
	print "You win!"
else:
	print "You lose!"

print "Your score: {}\nOpponent score: {}".format(your_score, enemy_score)
