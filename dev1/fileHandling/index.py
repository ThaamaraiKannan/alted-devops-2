# file = open("demo.txt", "a")
# print(file.write("\nSSSSSSSSs"))
# file.close()
# file = open("demo.txt", "rb")
# print(file.read())
# file.close()

# a -> append
# r -> read
# w -> write
# x -> new file create

# rt, r ->

# rb

with open("demo.txt", "xb") as f:
    file_read = f.read()
    print(file_read)
