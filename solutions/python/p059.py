"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
"""
from utils import read_file
from itertools import product
import string


def run():
    """
    Try every password possible, get rid of junk and filter.
    """
    encoded = map(int, read_file('data/p059 cipher1.txt'))

    # all possible passwords of length 3
    passwords = product(map(ord, string.lowercase), repeat=3)

    for password in passwords:
        decoded = ''
        for index, c in enumerate(encoded):
            dc = chr(c ^ password[index % len(password)])
            if dc in '${}#^@+=\|%*[]':
                break  # These chars probably don't exist in there
            decoded += dc
        else:
            if ' the ' in decoded:  # this already narrows down to 1
                return sum(map(ord, decoded))
