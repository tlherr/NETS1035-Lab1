# Thomas Herr
# 200325519
# NETS1035 Applied Cryptography

# 2.	Copy Ian’s Rot3 (Caesar cipher) program from the internet and make it work
# a.	Go to www.gcian.ca and find the rot13 program
# b.	Copy it onto your Kali system
# c.	Make the program work from the command line to encrypt or decrypt (sc)

import codecs
import sys, getopt


def main(argv):
    toencrypt = ''
    todecrypt = ''

    try:
        # options is the string of option letters that the script wants to recognize, with options that require an
        # argument followed by a colon
        opts, args = getopt.getopt(argv, "e:d:", ["encrypt=", "decrypt="])
    except getopt.GetoptError:
        print('question2.py -e <toencrypt> -d <todecrypt>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('question2.py -e <toencrypt> -d <todecrypt>')
            sys.exit()
        elif opt in ("-e",'--encrypt'):
            # Encrypting
            toencrypt = arg
        elif opt in ("-d", "--decrypt"):
            # Decrypting
            todecrypt = arg

    if(len(toencrypt)>0):
        print("Encrypting Phrase: ", toencrypt)
        print(codecs.encode(toencrypt, 'rot_13'))

    if(len(todecrypt)>0):
        print("Decrypting Phrase: ", todecrypt)
        print(codecs.decode(todecrypt, 'rot_13'))

if __name__ == "__main__":
   main(sys.argv[1:])