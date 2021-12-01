# https://github.com/hyperopt/hyperopt/wiki/FMin#12-attaching-extra-information-via-the-trials-object
from hyperopt import fmin, tpe, hp, STATUS_OK, STATUS_FAIL

def objective(x):
    return {'loss': x ** 2, 'status': STATUS_FAIL if False else STATUS_OK}

best = fmin(objective,
    space=hp.uniform('x', -10, 10),
    algo=tpe.suggest,
    max_evals=100)

print(best)