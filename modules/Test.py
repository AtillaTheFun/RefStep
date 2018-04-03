# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:21:18 2018

@author: h.gibb
"""

import GTC

x1 = GTC.ureal(2.42,0.19)
x2 = GTC.ureal(2.59,0.15)
x3 = GTC.ureal(2.45,0.19)
x4 = GTC.ureal(2.83,0.16)
x5 = GTC.ureal(2.65,0.20)

x6 = x1+x2+x3+x4+x5

print(GTC.uncertainty(x6))
print(GTC.value(x6)/5)

