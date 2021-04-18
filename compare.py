file = open("uncompressed.txt", "r")
data = file.read()
number_of_characters = len(data)
print("Uncompressed bits " + str(number_of_characters))

file = open("compressed.txt", "r")
data = file.read()
number_of_characters = len(data)
print("Compressed bits " + str(number_of_characters))
