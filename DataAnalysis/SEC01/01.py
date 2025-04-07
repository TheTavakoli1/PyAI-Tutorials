import sys
import time

start = time.time()


_list = list(range(100_000_000))

for i in _list:
    i += 1


end = time.time()

print(f"Time: {end - start} second")
print(f"size: {sys.getsizeof(_list) / (1024 * 1024)}, MB")