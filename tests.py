from bakit import defer

file = open("test.txt")

@defer(file.close)
def read():
   return file.read()

print(read())