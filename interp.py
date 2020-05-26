import numpy
from scipy import interpolate
import matplotlib.pyplot as plt



def interp(xi, x, y):
  yi = 0.0
  for i in range(4):
    li = 1.0
    for j in range(4):
      if(i != j):
        li = li * (xi - x[j]) / (x[i] - x[j])
    yi = yi + li * y[i]
  return yi

def stretch(x, y, l):
  x_out = numpy.linspace(x[0], x[-1], l)
  y_out = numpy.zeros((l,),)
  xn = 0
  for n in range(l):
    while(not (x_out[n] <= x[xn+1] and x_out[n] >= x[xn])):
      xn = xn + 1
    nn = xn
    if(nn < 0):
      nn = 0
    elif(nn + 4 > len(x)):
      nn = len(x) - 4
    y_out[n] = interp(x_out[n], x[nn:nn+4], y[nn:nn+4])      
  return x_out, y_out

def square_data(x, y, Z):
  if(len(x) == len(y)):
    return Z
  if(len(x) > len(y)):
    y_out = numpy.linspace(y[0], y[-1], len(x))
    Z_new = numpy.zeros((len(x), len(x),),)
    for i in range(len(x)):
      y_stretch, Z_new[i, :] = stretch(y, Z[i, :], len(x))
    return x, y_out, Z_new
  if(len(x) < len(y)):
    x_out = numpy.linspace(x[0], x[-1], len(y))
    Z_new = numpy.zeros((len(y), len(y),),)
    for i in range(len(y)):
      x_stretch, Z_new[:, i] = stretch(x, Z[:, i], len(y))
    return x_out, y, Z_new


nx = 8
ny = 50


x = numpy.linspace(-2.0, 2.0, nx)
y = numpy.linspace(-2.0, 2.0, ny)
Z = numpy.zeros((nx, ny,),)

for xi in range(nx):
  for yi in range(ny):  
    Z[xi,yi] = numpy.cos(x[xi] ** 2 + y[yi] ** 2)

x_new, y_new, Z_new = square_data(x, y, Z)
  

print(Z_new)
plt.plot(y, Z[0, :], 'ro-', y_new, Z_new[0, :], 'b-')
plt.show()







"""
for xi in range(nx):
  for yi in range(ny):  
    Z[xi,yi] = numpy.cos(x[xi] ** 2 + y[yi] ** 2)

print(y)
print(Z[0,:])
yp = numpy.linspace(-2.0, 2.0, 16)
yinterp = numpy.interp(yp, y, Z[0,:])
print(yinterp)

plt.plot(y, Z[0, :], 'ro-', yp, yinterp, 'b-')
plt.show()


for xi in range(nx):
  for yi in range(ny):  
    Z[xi,yi] = numpy.cos(x[xi] ** 2 + y[yi] ** 2)


f = interpolate.interp2d(x, y, Z, kind='cubic')

xnew = numpy.linspace(-2.0, 2.0, 31)
ynew = numpy.linspace(-2.0, 2.0, 31)
znew = f(xnew, ynew)
plt.plot(x, Z[:, 0], 'ro-', xnew, znew[:, 0], 'b-')
plt.show()

"""

