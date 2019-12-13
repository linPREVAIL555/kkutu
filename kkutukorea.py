running = True
s = 0
i = input("start ")
l = set([])
z = input("How many letters do you want? ")
w = int(z)

while running:
	x = input("")
	y = len(i)

	if len(x) == 0:
		running = False
	elif len(x) != w and x[0] == i[y-1]:
		print("Must be ",z," letters.")
		i = x
#	elif len(x) == 1:
#		print("Too short. Try again.")
	elif x in l:
		print("No repeats. Try again.")
	elif x[0] == i[y-1]:
		i = x
		l.add(x)
		s = s+1
	else:
		running = False
else:
	print ("Game over. Your score is ",s)
	print (l)
