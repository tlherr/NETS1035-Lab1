# Thomas Herr
# 200325519
# NETS1035 Applied Cryptography

# 4.	Create a base64 encoded message using python and the command line
# a.	Encode and Decode a base64 message from the linux shell (screenshots)
# b.	Encode and Decode the same message using pythons base64 library. (screenshots)

import base64
import sys, getopt


def main(argv):
    toencrypt = ''
    todecrypt = ''

    try:
        opts, args = getopt.getopt(argv, "e:d:", ["encrypt=", "decrypt="])
    except getopt.GetoptError:
        print('question4.py -e <toencrypt> -d <todecrypt>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('question4.py -e <toencrypt> -d <todecrypt>')
            sys.exit()
        elif opt in ("-e",'--encrypt'):
            # Encrypting
            toencrypt = arg
        elif opt in ("-d", "--decrypt"):
            # Decrypting
            todecrypt = arg

    if(len(toencrypt)>0):
        print("Encrypting Phrase: ", toencrypt)
        print(base64.b64encode(toencrypt.encode()))

    if(len(todecrypt)>0):
        print("Decrypting Phrase: ", todecrypt)
        print(base64.b64decode(todecrypt))

if __name__ == "__main__":
   main(sys.argv[1:])