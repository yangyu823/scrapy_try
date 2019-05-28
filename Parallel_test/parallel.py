from time import time
from math import sqrt
from joblib import Parallel, delayed

start = time()

# single-core code
sqroots_1 = [sqrt(i ** 5) for i in range(100)]

# parallel code
sqroots_2 = Parallel(n_jobs=2)(delayed(sqrt)(i ** 5) for i in range(100))

print(sqroots_1, "###", time() - start)
print(sqroots_2, "###", time() - start)
