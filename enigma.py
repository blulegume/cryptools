pi = [23,13,24,0,7,15,14,6,25,16,22,1,19,18,5,11,17,2,21,12,20,4,10,9,3,8]
##invPi = [3,11,17,24,21,14,7,4,25,23,22,15,19,1,6,5,9,16,13,12,20,18,10,0,2,8]
invPi = [pi.index(i) for i in range(0, len(pi))]

def encrypt(ptext, K, i): # assuming Z26
    if ptext:
        c = ord(ptext[0].upper())- 65
        z = (K + i - 1) % 26
        e = (pi[c] + z) % 26
        print 'c = {0}, z = {1}, e = {2}, pi[i-1]={3}'.format(c,z,e,pi[i-1])
        return chr(e+65) + encrypt(ptext[1:], K, i+1)
    return ""
    
def decrypt(ctext, K, i): # assuming Z26
    if ctext:
        y = ord(ctext[0].upper()) - 65
        z = (K + i - 1) % 26
        pos = (y-z) %26
        e = invPi[pos]
        #print invPi[pos]
        print 'y = {0}, z = {1}, e = {2}, pos={3}, invPi[pos] = {4}'.format(y,z,e,pos,invPi[pos])
        return chr(e+65) + decrypt(ctext[1:], K, i+1)
    return ""

def key_search(ctext):
    for i in range(26):
        print ' K = {0}\t'.format(i) + decrypt(ctext.upper(), i, 1)