'''
Linear Congruential Generator

formula: Xn+1 = (a*Xn + c) mod m

X0 is the "seed" value.
To randomize X0, use system variables like pid,time.

Note:
This is a weak pseudo random number generator, refer only to understand the concept.
Not recommended for practical applications.
'''

import os,time

class LCGPseudoRandomGenerator:

    #using C++ 11's minstd_rand values
    def __init__(self, a=48271, c=0, m=2**31-1, seed=None):
        self.a = a
        self.c = c
        self.m = m
        if seed is None:
            self.x0 = int(os.getpid() + time.time())
        else:
            self.x0 = seed
        self.x_prev = (self.a*self.x0 + self.c) % self.m
    
    def generate_number(self, low=None, high=None):
        self.x_prev = (self.a*self.x_prev + self.c) % self.m
        if low==None and high==None:
            return self.x_prev
        return int((self.x_prev / (self.m-1)) * (abs(high-low)) + low)
    
lcg = LCGPseudoRandomGenerator()

print(lcg.generate_number(0,100))
print(lcg.generate_number(0,100))
print(lcg.generate_number(0,100))
print(lcg.generate_number(0,100))
print(lcg.generate_number(0,100))