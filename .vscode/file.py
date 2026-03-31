with open("a.txt", "r") as file1, open("b.txt", "r") as file2:
data1 = file1.read()
data2 = file2.read()
with open("combined.txt", "w") as outfile:
outfile.write(data1 + "\n" + data2)
print("Files merged successfully!")