import time 
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials 
from sigopt.hyperopt import upload_trials 
def objective(args): 
  x, = args 
  return { 
    "loss": x ** 2, 
    "status": STATUS_OK, 
    "eval_time": time.time(), 
    "other_stuff": {"type": None, "value": [0, 1, 2]}, 
  } 
trials = Trials() 
space = (hp.uniform("x", -10, 10),) 
best = fmin(objective, space=space, algo=tpe.suggest, max_evals=1, trials=trials) 
upload_trials(project="project-name", trials=trials) 
 