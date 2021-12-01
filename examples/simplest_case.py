#https://github.com/hyperopt/hyperopt/wiki/FMin#11-the-simplest-case
from hyperopt import fmin, tpe, hp
best = fmin(fn=lambda x: x ** 2,
    space=hp.uniform('x', -10, 10),
    algo=tpe.suggest,
    max_evals=5)
print(best)