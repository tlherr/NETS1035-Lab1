# Thomas Herr
# 200325519
# NETS1035 Applied Cryptography

# 1.	Create a python program that takes a string and prints out the   first,middle  and last characters.
# a.	The program should take an input,value = input(), or use argv
# b.	Example input is hello, output is “hlo”

while True:
    try:
        name = input("Please enter a string: ")
        if not name:
            raise ValueError('Empty String Given')
    except ValueError as e:
        print("Sorry, I didn't understand that.")
        print(e)
        continue
    else:
        break

length = len(name)
half = int(length/2)

print(name[0],name[half],name[length - 1], sep='')


