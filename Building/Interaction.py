# import numpy as np
# N = 800*10**3
# b = 0.3
# h = 0.3
# M = 12*10**3
# fcu = 20*10**6
# Asbh = -0.01
# d1h=0.2
# d1 = h*d1h

# d = h-d1

# dh=d/h
# print(d,d1,dh)

# xvals = np.arange(0,0.31,0.01)

# for x in xvals:
# 	xh = x/h
# 	eqnleft1 = [Asbh,-Asbh]
# 	eqnleft2 = [Asbh*(0.5-d1h),-Asbh*(0.5-dh)]

# 	eqnr1 = N/(b*h)-0.4*fcu*xh
# 	eqnr2 = M/(b*h**2)-0.4*fcu*xh*(0.5-0.45*xh)

# 	left = np.array([eqnleft1,eqnleft2])
# 	# print(left)
# 	right = np.array([eqnr1,eqnr2])
# 	# print(right)

# 	y = np.linalg.solve(left,right)
# 	print(x,y/10**6)



# def Icurve()
# from math import pi as pi
# import numpy as np

# cc = 0.0035
# cl = 40
# rod = 16
# d1 = cl+rod/2
# b = 300
# h = 300
# n = 4
# p = ((pi*rod**2/4)*n)/(b*h)
# d1h=d1/h
# d1 = h*d1h
# fy = 250
# fcu = 25
# E = 200000
# d = h-d1
# dh = d/h
# fyE = fy/210000
# bp = cc*d/(fyE+cc)
# N = 800
# M = 12
# load = []
# moment = []
# print(p)
# print(bp)
# print(d/h)
# for c in range(1,h+1):
# 	es = cc*(d-c)/c
# 	if abs(es)>fyE:
# 		fs = 0.95*fy
# 	else:
# 		fs = es*E
# 	esc = cc*(c-d1)/c
# 	if abs(esc)>fyE:
# 		fsc = 0.95*fy
# 	else:
# 		fsc = esc*E

# 	Nbh = 0.4*fcu*c/h + p*(fsc) - p*(fs)
# 	Mbh = 0.4*fcu*c/h*(0.5-0.45*c/h) + p*fsc*(0.5-d1h)-p*fs*(0.5-dh)
# 	load.append(Nbh/fcu)
# 	moment.append(Mbh/fcu)
# 	print(c,Nbh/fcu,Mbh/fcu)

# print(load)
# print(load)







# x = 0.1791
# xh = x/h
# eqnleft1 = [Asbh,-Asbh]
# eqnleft2 = [Asbh*(0.5-d1h),-Asbh*(0.5-dh)]

# eqnr1 = N/(b*h)-0.4*fcu*xh
# eqnr2 = M/(b*h**2)-0.4*fcu*xh*(0.5-0.45*xh)

# left = np.array([eqnleft1,eqnleft2])
# # print(left)
# right = np.array([eqnr1,eqnr2])
# # print(right)

# y = np.linalg.solve(left,right)
# print(x,y/(10**6))

# fck = 20
# D = 300

# k = 1
# g = 0.446*fck*(4/(7*k-3))**2


# A = 0.446*fck*D-g/3*4/7*D

# M = 0.446*fck*D**2/2-8/49*g*D**2
# print((M/D)/A)
# print((M)/A)

from math import pi as pi
import numpy as np

cc = 0.0035
cl = 40
rod = 16
d1 = cl+rod/2
b = 300
h = 300
n = 10
p = ((pi*rod**2/4)*n)/(b*h)
p1 = 0.89
d1h=d1/h
d1 = h*d1h
fy = 250
fcu = 25
E = 200000
d = h-d1
dh = d/h
fyE = fy/210000
bp = cc*d/(fyE+cc)
load = []
moment = []
fst = []
fct = []
est = []
esct = []
print('p',p)
print('bp',bp)
print('b',b)
print('d',d)
print('h',h)
print('d1',d1)

print('d1/h',d1h)
print('d/h',dh)
print(f"check strain in tension {cc*(h-bp-d1)/bp-fyE:0.005f}")
print(f"check strain in compression {cc*(bp-d1)/bp-fyE:0.05f}")

for c in range(1,h+1):
#     es = cc*(d-c)/c
    es = cc*(h-c-d1)/c
    
#     print('es',es)
    if abs(es)>fyE:
        if es<0:
            fs = -0.95*fy
        else:
            fs = 0.95*fy
    else:
        fs = es*E
    
#     esc = cc*(c-d1)/c
    esc = cc*(c-d1)/c
#     print('esc',esc)
    if abs(esc)>fyE:
        if esc<0:
            fsc = -0.95*fy
        else:
            fsc = 0.95*fy 
    else:
        fsc = esc*E
    Nbh = 0.4*fcu*c/h + p*(fsc) - p*(fs)
    Mbh = 0.4*fcu*c/h*(0.5-0.45*c/h) + p*fsc*(0.5-d1h)-p*fs*(0.5-dh)
    est.append(es)
    esct.append(esc)
    fst.append(fs)
    fct.append(fsc)
    load.append(Nbh/fcu)
    moment.append(Mbh/fcu)

print(f"Neut\t\tes\t\t\tFS\t\t\t esc\t\t\t FSC\t\tLoad\t\tMoment")

for i in range(len(load)):
	print(f"{i+1}\t\t{est[i]:.06f}\t\t{fst[i]:.02f}\t\t{esct[i]:.06f}\t\t{fct[i]:.02f}\t\t{load[i]:.02f}\t\t{moment[i]:.02f}")
    # print(c,'fs',fs,'fsc',fsc,'Nbh',Nbh,'Mbh',Mbh)


# loads = np.array([load])
# moments = np.array([moment])
# print(moments.max())