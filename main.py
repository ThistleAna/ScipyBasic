# Scipy is another important package in Python
# Import scipy before using
import scipy as sp
# import sub packages that we will use

from scipy import integrate
from scipy import cluster
from scipy import fftpack
from scipy import special

# use help() function to see sub packages
# help()
# to make reference to scipy use sp
# to see information of the subpackage fftpack
# sp.info(fftpack)
# sp.source(cluster)

# use the special function to access math functions
func = special.kelvin(15)
print(func)

func1 = special.exp10(5)
print(func1)

func2 = special.xlogy(2,10)
print(func2)

func3 = special.sindg(105)
print(func3)

# Use integrate function to integrate variables
var1 = lambda a:a**3
function1 = integrate.quad(var1,0,6)
print(function1)
# Double integration of two variable x and y
var2 = lambda y, x:x*y**4
function2 = integrate.dblquad(var2,0,6,lambda x:0, lambda x:1)
print(function2)