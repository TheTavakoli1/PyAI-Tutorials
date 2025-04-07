import numpy as np
import time
import sys

start = time.time()


X = np.arange(100_000_000) + 1

print(type(X))
end = time.time()

print(f"time: {end - start} second")
print(f"size: {sys.getsizeof(X) / (1024 * 1024)} MB")