import os
ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system('git add commit.py')
	os.system(f'git commit --amend --date="2018-09-11 11:11:11"')	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
 
# git commit --allow-empty -m "New Commit at: $(date)"
