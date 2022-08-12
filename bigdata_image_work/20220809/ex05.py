from cgi import print_arguments
from doctest import REPORTING_FLAGS
import numpy as np

a = np.array([1,2,3,4])
print(a.shape)

a = a.reshape(-1,2)
print(a.shape)

print(a)