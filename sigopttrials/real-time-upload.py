import time 
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials 
from sigopt.hyperopt import SigOptTrials 
def objective(args): 
  x, = args 
  return { 
    "loss": x ** 2, 
    "status": STATUS_OK, 
    "eval_time": time.time(), 
    "other_stuff": {"type": None, "value": [0, 1, 2]}, 
  } 
space = (hp.uniform("x", -10, 10),) 
trials = SigOptTrials(project="project-name") 
best = fmin(objective, space=space, algo=tpe.suggest, max_evals=1, trials=trials)