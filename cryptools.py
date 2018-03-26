## returns a positive equivalent for a negative integer in Zm
def pos(a,m):
    return a % m

## returns the negative equivalent for a positive integer in Zm
def neg(a,m):
    if a > 0:
        a = 0 - m + pos(a,m)
    return a

## finds greatest common divisor of two numbers
def gcd(a,b): # a > b
    if b > a:
        return gcd(b,a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

## in Zm, finds and lists all invertible numbers
def find_invertibles(m):
    invertibles = []
    for i in range(1,m):
        f = gcd(m,i)
        #print "gcd({},{}):\t{}".format(m,i,f)
        if f == 1:
            invertibles.append(i) 
    #print "invertible numbers in Z({}): {}".format(m,invertibles)
    return len(invertibles)

## finds inverse of a number in Zm
def inverse_mod_m(a,m):
    if gcd(m,a) != 1:
        return -1
    return pos(extended_euclidian(m,a,0,1),m)

## helper fcn for inverse_mod_m. Does not find s (but could)
def extended_euclidian(a,b,tn_2,tn_1):
    if a % b == 0:
        return tn_1 #is this right?
    q = a / b
    tn = tn_2 - (q * tn_1)
    return extended_euclidian(b, a%b,tn_1, tn)

## helper fcn for pollard p-1 algorithm
## returns b^e in Zn (useful for long numbers, not really needed
## in python thanks to long()
def p_helper(b,e,n):
    ans = b
    for i in range(1,e):
        ans = (ans*b) % n
    return ans

## helper fcn for pollard p-1 algorithm
## could be conbined with p_helper
## returns a^(B!)
def p(a,B,n):
    ans = a
    for i in range(1,(B+1)):
        #q = ans
        ans = p_helper(ans,i,n)
        #print '{0}^{1} =\t\t{2}'.format(q,i,ans)
    return ans

## pollard p-1 algorithm
## fatorizes large composite numbers into two primes.
## multiple possible returns, choose accordingly
def pollard(n,B):
    a = 2
    for i in range (a,n):
        #print 'Let a={0}'.format(a)
        ans = gcd((p(a,B,n))-1,n)
        if ans > 1: 
            #return ans
            ## could return a tuple with both factors...and a?
            #return (a, ans, n/ans)
            print 'this is the answer: {0} {1}'.format(ans, n/ans)
            return (ans, n/ans)
            ## could also return a dictionary...
            #return {'a': a, 'gcd': ans, 'quotient': n/ans} 
    return -1




