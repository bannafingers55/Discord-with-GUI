import os
from bot import FilterBot

f = open("path.path", "r")
path = f.read()
f.close()
print(path)
if os.path.isdir("data/") == False:
	print("Creating data directory")
	os.mkdir("data/")

try:
	f = open(path, "r")
	f.close()

except:
	f = open(path, "w+")
	token = input("No token found, please input token:\n")
	f.write(token)
	f.close()
	print("Token saved")
	time.sleep(1)

print("Booting...")

b = FilterBot()
b.run()
