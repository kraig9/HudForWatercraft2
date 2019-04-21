filename = "capturefile"
file = open(filename, "r")
for line in file:
	print(repr(line))

