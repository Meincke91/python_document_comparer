import os

with open("dummy_files_1.txt","w") as f:
	for x in range(1,100000):
		f.write("file" + str(x) + "\n")

with open("dummy_files_2.txt","w") as f:
	for x in range(1,100000):
		if not (x % 100 == 0):
			f.write("file" + str(x) + "\n")