import numpy as np
temp = np.array([32,35,37,40,34,31,30])
print("temp on mon:",temp[0])
print("temp from tue to sunday:",temp[1:])
print("highet temperature:",np.max(temp))
print("lowest temperature:",np.min(temp))
print("average temperature:",np.mean(temp))
print("deviation:",np.std(temp))
