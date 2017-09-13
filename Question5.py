# Thomas Herr
# 200325519
# NETS1035 Applied Cryptography

# ADVANCED
#
# This question is not required, but is a challenge.
# Find a built-in python function that exists to decrypt this message:
#
# Dtz rzxy qnpj ijhwduynsl ymnslx?

encrypted = "Dtz rzxy qnpj ijhwduynsl ymnslx?"

# Attempt +40 to -40 char shift

# @ref: http://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/
def rot_by(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    # Using maketrans to map each ascii character to ascii position of n modifier start/end uppercase and lowercase
    # essentially take the ascii table and map it to a slice of the table modified by our n value. So any character will
    # map to its equivilent n positions ahead or behind in the ascii table (thus implementing rot(n))
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

for x in range(-40,40):
    print("Using Shift Value: ", x)
    print(rot_by(x)(encrypted))