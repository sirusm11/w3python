f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")


f = open("myfile.txt", "x")