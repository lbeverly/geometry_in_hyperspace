# unit sphere r = 1
# x^2 + y^2 + z^2 = r^2
# generating points to plot a sphere

import math

# r = 1

# math.sin(theta)
# math.cos(theta) 
# math.sin(phi)
# math.cos(phi) (for z we can skip calculating cos, because we have x, y)

# (theta, phi, r)   r = 1

# beta = phi for below
# alpha = theta

# x = r cos beta sin alpha
# y = r cos beta cos alpha
# z = r sin beta 
# R^3 polar to cartesian conversion
def polar_to_cartesian(alpha, beta, r):
    x = r *  math.cos(beta) * math.sin(alpha)
    y = r * math.cos(beta) * math.cos(alpha)
    z = r * math.sin(beta) 
    return (x, y, z)


r = 1

for alpha in range(0,180,10):
    for beta in range(0,360,10):
        coords = polar_to_cartesian(math.radians(alpha), math.radians(beta), r)
        print('{} {} {}'.format(*coords))


