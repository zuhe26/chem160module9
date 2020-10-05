import math
from numpy import isclose
a=3.
if math.sqrt(a)**2 != a:
    print("WTH??")
tol=1e-12
if abs(math.sqrt(a)**2-a) > tol:
     print("WTH again!?")
from numpy import isclose
if isclose(math.sqrt(a)**2,a):
    print("Close enough!")
