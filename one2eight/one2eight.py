import random

SIZE = 3

def cetak():
	global number
	print """
	###################
	#     #     #     #
	#  {}  #  {}  #  {}  #
	#     #     #     #
	###################
	#     #     #     #
	#  {}  #  {}  #  {}  #
	#     #     #     #
	###################
	#     #     #     #
	#  {}  #  {}  #  {}  #
	#     #     #     #
	###################
	""".format(number[0], number[1], number[2], number[3], number[4], number[5], number[6], number[7], number[8])

def move(inpud, space):
	global number
	if inpud == 'w':
		if space / SIZE == 0:
			z = 0
		else:
			number[space] = number[space-SIZE]
			number[space-SIZE] = ' '
	elif inpud == 'a':
		if space % SIZE == 0:
			z = 0
		else:
			number[space] = number[space-1]
			number[space-1] = ' '
	elif inpud == 's':
		if space / SIZE == SIZE-1:
			z = 0
		else:
			number[space] = number[space+SIZE]
			number[space+SIZE] = ' '
	elif inpud == 'd':
		if space % SIZE == SIZE-1:
			z = 0
		else:
			number[space] = number[space+1]
			number[space+1] = ' '
	else:
		z = 0

	return number

number = [str(i) for i in range(1, 9)]
muv = 'wasd'
number.append(' ')

ans = ''
for i in range(100):
	step = random.choice(muv)
	space = number.index(' ')
	move(step, space)
	ans += step
for i in 'sdsd':
	space = number.index(' ')
	move(i, space)
	ans += i

cetak()

while True:
	space = number.index(' ')
	inpud = raw_input("Your move: ").lower()
	move(inpud, space)
	cetak()
	if "".join(number) == "12345678 ":
		flag = open('flag.txt').read()
		print "You win!\n%s" % (flag)
		exit()
