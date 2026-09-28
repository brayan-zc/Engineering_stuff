import math

#Part2a
def reason(a, T):
    return T**2/a**3

SA_planets=[0.38709927, 0.72333566, 1.00000261, 1.52371034, 5.20288700, 9.53667594, 19.18916464, 30.06992276]
OP_planets=[0.2408467, 0.61519726, 1.0000174, 1.8808476, 11.862615, 29.447498, 84.016846, 164.79132]
planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for a, T, p in zip(SA_planets, OP_planets, planets):
    print(p, "'s reason:", reason(a, T))

#Part2b
def mass(T, a, G):
    return ((4*(math.pi**2)*(a**3))/(G*(T**2))) 
G=6.67430e-11
Neptune=102.4092e24

SA_Nept_Sat=[354800, 48200, 50100, 52500, 62000, 73500, 117600, 105300, 5513900, 16590500, 47646600, 22239900, 23499900, 49897800, 23414700, 50700200]
OP_Nept_Sat=[5.876994, 0.293980, 0.311078, 0.334656, 0.428744, 0.554989, 1.122315, 0.950390, 360.133039, 1879, 9149, 2919, 3168, 9805, 3151, 10043]
m_SA_NS=[a*1000 for a in SA_Nept_Sat]
s_OP_NS=[T*86400 for T in OP_Nept_Sat]

print("SA in meters:", [m for m in m_SA_NS])
print("OP in seconds:", [s for s in s_OP_NS])

results=[mass(T, a, G) for a, T in zip(m_SA_NS, s_OP_NS)]
neptune_exp=sum(results)/len(results)
print("Neptune's calculated  mass:", neptune_exp, "kg")

diference_m=(math.fabs(Neptune-neptune_exp))
print("the diference between the known and calculated mass is:", diference_m, "kg")
error_m=(math.fabs(neptune_exp-Neptune)/Neptune)*100
print("the error in the mass calculation is:", error_m, "%")

#Part2c
def reason(SA, OP):
    return SA**3/OP**2

def WASP76_mass(OP, SA, G):
    return ((4*(math.pi**2)*(SA**3))/(G*(OP**2))) 
G=6.67430e-11

OP=1.80988198*86400
SA=0.0330*149597870700

WASP76_solarmass=WASP76_mass(OP, SA, G)/1.989e+30
WASP76_mass=WASP76_mass(OP, SA, G)

print("the reason for WASP-76b is:", reason(SA, OP))
print("the mass of WASP-76 is:", WASP76_solarmass, "M_sun")
print("the mass of WASP-76 is:", WASP76_mass, "kg")

def Newton(G, WASP76_mass):
    return ((G*WASP76_mass)/(4*(math.pi**2)))
print("the Newton's constant for WASP-76 is:", Newton(G, WASP76_mass))

#Part3
def reces_vel(z, c):
    return z*c
c=299792458/1000
H=67.4

redshift=[8.678800, 2.190000, 6.418900, 10.957000, 14.179600]
cz=[2601839, 656545, 1924338, 3284826, 4250937]
Hubble_d=[38376.91, 9681.85, 28385.27, 48450.53, 62696.47]

vel=[reces_vel(z, c) for z in redshift]
print("the aproximated recession velocities are:", [v for v in vel])
distance=[v/H for v in vel]

print("these are the calculated distances:", [d for d in distance])
print("diferences between the calculated distances and the Hubble distance are:", [math.fabs(d-Hd) for d, Hd in zip(Hubble_d, distance)])


