# encrypt word using Autokey cipher (use k := n upon calling)
def encrypt(word, n): # assumes Z26
    if word:
        c = ord(word[0].upper()) - 65 
        r = (c + n) % 26 + 65
        return chr(r) + encrypt(word[1:], c)
    return ""

# decrypt word using Autokey cipher (use k := n upon calling)
def decrypt(word, n): # assumes Z26
    if word:
        c = ord(word[0].upper()) - 65
        r = (c - n) % 26
        return chr(r+65) + decrypt(word[1:], r)
    return ""

# use exhaustive search on ctext with Autokey cipher to find k
def key_search(ctext):
    for i in range(26):
        print ' i = {0}\t'.format(i) + decrypt(ctext.upper(), i)

def helper(ctext,k):
    lst = []
    lst1 = []
    for c in ctext:
        lst.append(ord(c)-65)
        lst1.append(c)
    print lst, '\n', lst1
    ptext = decrypt(ctext,k)
    lst = []
    lst1 = []
    for p in ptext:
        lst.append(ord(p)-65)
        lst1.append(p)
    print lst, '\n', lst1, '\n', ptext