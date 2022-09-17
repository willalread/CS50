import sys

lines = []

try:
    with open(sys.argv[1]) as file:
        for line in file:
            lines.append(line.lstrip())
except FileNotFoundError:
    sys.exit

counter = 0
for line in lines:
    if not line.startswith("#") and line.strlen > 0:
        counter += 1

print(counter)