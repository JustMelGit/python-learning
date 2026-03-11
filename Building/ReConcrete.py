import math
from math import pi as pi

# perConc = 7
# b = 250
# N = 5
# dia = 20
# cc = 25
# D = 400
# perSteel = 140
# d = D-cc-dia/2
# Ast = N*pi*dia**2/4
# P = 100*Ast/(b*d)
# M = 280/(3*perConc)

# k = -P/100*M +(((P/100)**2*M**2)+(2*(P/100)*M))**(0.5)
# j = 1-k/3
# LA = j*d
# x = k*d
# MRst  = Ast*perSteel*LA
# MRconc = b/2*x*perConc*LA
# print(Ast)
# print(P)
# print(M)
# print(k)
# print(k*d)
# print(MRst)
# print(MRconc)

b = 250
N = 4
dia = 16
cc = 25
D = 400
fck  = 20
fy = 415
d = D-cc-dia/2
Ast = N*pi*dia**2/4
xdr = 0.48
Pt = 0.36*xdr*20*100/(0.87*415)
P = Ast*100/(b*d)

mSF = 0.87*fy*(P/100)*(1-(P/100*fy/fck))*b*d**2

mCF = 0.36*fck*b*d**2*xdr*(1-0.42*xdr)
# print(41.3*fck*xdr/fy)

print(Ast)
print(P)
print(Pt)
print(mSF)
print(mCF)
