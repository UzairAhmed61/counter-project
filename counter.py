import os

file = "count.txt"

# Agar file exist nahi karti to start 2 se
if not os.path.exists(file):
    num = 2
else:
    with open(file, "r") as f:
        num = int(f.read())

print("Result:", num)

num += 2

with open(file, "w") as f:
    f.write(str(num))
