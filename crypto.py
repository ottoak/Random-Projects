# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:55:25 2020

@author: Alex
"""
import random
import string
import time

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, rsa, padding


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)

strings = []
for i in range(0,10000):
    strings.append(str.encode(get_random_string(20)))


#============= EC =============
private_key_EC = ec.generate_private_key(
     ec.SECP256R1()
)

t0=time.time()
for i in range(0,len(strings)):
    signature_EC = private_key_EC.sign(
         strings[i],
         ec.ECDSA(hashes.SHA256())
    )
t1=time.time()

print("{}s".format(t1-t0))

#============= RSA =============
private_key_RSA = rsa.generate_private_key(
     public_exponent=65537,
     key_size=3072,
)

t2=time.time()
for i in range(0,len(strings)):
    signature_RSA = private_key_RSA.sign(
         strings[i],
         padding.PSS(
             mgf=padding.MGF1(hashes.SHA256()),
             salt_length=padding.PSS.MAX_LENGTH
         ),
         hashes.SHA256()
    )
    
t3=time.time()
print("{}s".format(t3-t2))