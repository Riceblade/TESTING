import os
ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
	print('okokok132123')
 git commit --date="100000 day ago" -m "Your commit message" 
 git commit --date="18024 day ago" -m "troll" 
# git commit --allow-empty -m "New Commit at: $(date)"
