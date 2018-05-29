from cryptools import gcd,inverse_mod_m,pollard
from math import log,floor,ceil

# finds block number ^2^x
def blocka(n,block,h):
    bp2p = [block]
    for i in range(1, h+1):
        bp2p.append((block ** 2) % n)
        block = bp2p[i]
    #print 'bp2p:', bp2p
    return bp2p

# returns a list on integers that, when added together as powers of p,
# equal n
# i.e., 4913 = 2^12 + 2^9 + 2^8 + 2^5 + 2^4 + 2^0
# find_pwr_factors(4913,2) returns [12,9,8,5,4,0]
def find_pwr_factors(n,p):
    b = []
    vals = []
    while n:
        b.append(n % p)
        n = n/p
    for k in range(len(b)):
        if b[k]: vals = [k] + vals
    return vals

# reduce powers into one single block number (d or e)
def redux(lst,n):
    def mult(a,b): return (a*b)% n
    return reduce(mult,lst,1)
    
#   turn blocks of characters into one integer in Zn
def block_to_num(block,n):
    lst = []
    i = len(block)-1
    for c in block:
        lst.append((ord(c.upper())-65) * 26**i)
        i = i - 1
        #print '{0} = {1} * 26^{2}'.format(c,ord(c.upper())-65, i)
    def add(a,b): return a + b
    return reduce(add,lst,0) % n

# turn integer n into block of characters of size bs
def num_to_block(n,bs):
    lst = []
    vals = []
    
    while n != 0:
        lst.append(n % 26)
        n = n/26
    for i in lst:
        vals = [chr(i+65)] + vals
    if len(vals) < bs: vals = ['A'] + vals
    return ''.join(vals)   

# gets relevant exponent values from list of all exponent values (pwrs)
def trim_pwrs(pwrs,k):
    new_k = []
    for i in range(len(pwrs)):
        if i in k:
            new_k = [pwrs[i]] + new_k
    return new_k

def decrypt(n,b,block_nums):
    N = pollard(n,10) # is 10 enough?
    p = N[0]
    q = N[1]

    Phi_n = (p-1) * (q-1)
    a = inverse_mod_m(b,Phi_n)
    
    pbs = floor(log(n,26))

    k = find_pwr_factors(a,2)
    h = k[0] # should be highest value

    ptext = []
 
    for bnum in block_nums:
        bpwrs = trim_pwrs(blocka(n,bnum,h),k)
        ptext.append(num_to_block(redux(bpwrs,n),pbs))
    return ''.join(ptext)

# breaks up plaintext into properly sized blocks for encryption
def blockify(ptext,pbs):
	if ptext == '':
		return []
	return[ptext[:pbs]] + blockify(ptext[pbs:],pbs)

def encrypt(p,q,b,ptext):
	n = p*q
	cbs = int(ceil(log(n,26)))
	pbs = int(floor(log(n,26)))
	k = find_pwr_factors(b,2)
	h = k[0]

	blocks = blockify(ptext,pbs)
	ctext = []
	for block in blocks:
		bnum = block_to_num(block,n)
		bpwrs = trim_pwrs(blocka(n,bnum,h),k)
		ctext.append(redux(bpwrs,n))
	return ctext
