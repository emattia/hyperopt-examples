#https://github.com/hyperopt/hyperopt/wiki/FMin#11-the-simplest-case
from hyperopt import fmin, rand, hp
import hyperopt
best = fmin(fn=lambda x: x ** 2,
    space=hp.uniform('x', -10, 10),
    algo=rand.suggest,
    max_evals=5)
print(best)