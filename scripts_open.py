with open("tmp/hello", 'w') as file:
    file.write("Linda!")

with open("tmp/hello_extend", 'a') as file:
    file.write("Sarah!")

with open("tmp/hello_once", 'x') as file:
    file.write("Hello stanger!")

