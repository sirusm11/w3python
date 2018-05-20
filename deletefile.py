import os
#os.remove("myfile.txt")

if os.path.exists("myfile.txt"):
	os.remove("myfile.txt")
	print("myfile.txt deleted.")
else:
	print("The file does not exits")
	
os.rmdir("new")
	