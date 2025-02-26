# file input and output

# read a file
with open('test.txt', 'r') as f:
    print(f.read())

# write a file
with open('test.txt', 'w') as f:
    f.write('hello world')

# append a file
with open('test.txt', 'a') as f:
    f.write('hello again')

