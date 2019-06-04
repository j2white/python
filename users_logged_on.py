import psutil
user_list = psutil.users()
for x in users:
	print(x)