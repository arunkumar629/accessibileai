import random
score=0
while True:
	run=int(input("Enter your run"))
	opponent=random.randint(1,6)
	print("opponent run",opponent)
	if run==opponent:
		break
	else:
		score=score+run

print("your score",score)