import sys
sys.path.append('../../code/bin/Python/')

import MatrixElementbbWW


pa = [250.,0.,0.,250.]
pb = [250.,0.,0.,-250.]
p1 = [37.3187611814334,-14.68426080083153,-33.26675246773233, 8.38961269074130]
p2 = [77.3822049733058,-7.601837186355866,-72.83979503528143, 24.9916381444082]
p3 = [212.302258058168,-120.8666054041759, 131.7502214736349,-81.5144648226089]
p4 = [172.996775787093, 143.1527033913634,-25.64367397062112, 48.1332139874593]

amplitude = MatrixElementbbWW.M(pa, pb, p1, p2, p3, p4)

print()
print()
print(' INPUT')
print()
print("    pa = ", pa)
print("    pb = ", pb)
print("    p1 = ", p1)
print("    p2 = ", p2)
print("    p3 = ", p3)
print("    p4 = ", p4)
print()
print()
print(' OUTPUT')
print()
print("  --------------------------------------------------------------------------------")
print("    diagram                helicity                      amplitude"           )
print("  --------------------------------------------------------------------------------")
print("       1             [1, -1, 1, -1, 1,  1]      {x.real:e} + {x.imag:e} i".format(x=amplitude[0][0]))
print("       1             [1, -1, 1, -1, 1,  0]      {x.real:e} + {x.imag:e} i".format(x=amplitude[1][0]))
print("       1             [1, -1, 1, -1, 1, -1]      {x.real:e} + {x.imag:e} i".format(x=amplitude[2][0]))
print()
print("       2             [1, -1, 1, -1, 1,  1]      {x.real:e} + {x.imag:e} i".format(x=amplitude[0][1]))
print("       2             [1, -1, 1, -1, 1,  0]      {x.real:e} + {x.imag:e} i".format(x=amplitude[1][1]))
print("       2             [1, -1, 1, -1, 1, -1]      {x.real:e} + {x.imag:e} i".format(x=amplitude[2][1]))
print("  --------------------------------------------------------------------------------")
print()
print()
