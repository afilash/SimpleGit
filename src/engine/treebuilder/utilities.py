import hashlib
import random
import time


def randseq(seqlength=0):
    if seqlength > 12:
        raise ValueError("Seqlength should be less than 12.")
    begin= 10**seqlength
    end = 10**(seqlength+1) -1
    return random.randint(begin, end)

def genhash(seedint , leng = 0):
    if leng > 20 :
        raise ValueError("Length should be less than 12.")
    hash = hashlib.sha1()
    hash.update(str(time.time()) + str(seedint ))
    #print hash.hexdigest()
    return hash.hexdigest()[:leng]