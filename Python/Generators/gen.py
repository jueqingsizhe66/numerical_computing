from itertools import izip, compress

def bin_combinations(n):
    s = len(n)

    b = 0
    while b < 2**s:
        yield [i for i, v in izip(n, reversed('{0:b}'.format(b))) if v == '1']
        b += 1

def binary_gray(seq):
    """Return a binary gray code.  Does not yield an empty set!"""
    pool = tuple(seq)
    
    #We are subtracting one from the bit_length, one from the index
    n = len(pool) - 2
    
    old = (0 >> 1) ^ 0
    for i in xrange(1, 2**(n + 1)):
        new = (i >> 1) ^ i
        ind = n - (old ^ new).bit_length()
        yield pool[ind], bool(new & (1 << (n - ind)))
        old = new
        
def gray_combinations(n):
    s = len(n)
    t = [0]*s
    yield list(compress(reversed(n), t))

    final = [1]+[0]*(s-1)
    while t != final:
        if sum(t) % 2 == 0:
            t[-1] = (t[-1]+1) % 2
        else:
            for i, j in enumerate(reversed(t), 1):
                if j:
                    t[-i-1] = (t[-i-1]+1)%2
                    break

        yield list(compress(reversed(n), t))

def quickperm(seq, r):
    seq = list(set(seq))

    n = len(seq)
    p = range(n)

    i = 1
    while i < n:
        p[i] -= 1
        if i % 2 == 1:
            j = p[i]
        else:
            j = 0

        seq[j], seq[i] = seq[i], seq[j]
        i = 1
        while p[i] == 0:
            p[i] = i
            i += 1
        yield p

