from hyperopt import hp

### ALL TYPES IMPORTED IN hyperopt.hp
'''
from .pyll_utils import hp_choice as choice
from .pyll_utils import hp_randint as randint
from .pyll_utils import hp_pchoice as pchoice

from .pyll_utils import hp_uniform as uniform
from .pyll_utils import hp_uniformint as uniformint
from .pyll_utils import hp_quniform as quniform
from .pyll_utils import hp_loguniform as loguniform
from .pyll_utils import hp_qloguniform as qloguniform

from .pyll_utils import hp_normal as normal
from .pyll_utils import hp_qnormal as qnormal
from .pyll_utils import hp_lognormal as lognormal
from .pyll_utils import hp_qlognormal as qlognormal
'''

### space parameter description in hyperopt.fmin
'''
space : hyperopt.pyll.Apply node or "annotated"
        The set of possible arguments to `fn` is the set of objects
        that could be created with non-zero probability by drawing randomly
        from this stochastic program involving involving hp_<xxx> nodes
        (see `hyperopt.hp` and `hyperopt.pyll_utils`).
        If set to "annotated", will read space using type hint in fn. Ex:
        (`def fn(x: hp.uniform("x", -1, 1)): return x`)
'''

### case 1 - hyperopt.pyll.Apply node
### pyll.Apply represents a symbolic application of a symbol to args
### pyll.SymbolTable has methods tht allocate Apply nodes
### scope = SymbolTable()

### hp types
### hp_pchoice --> categorical 
### hp_choice --> categorical
### hp_randint --> int
### hp_uniform --> double
### hp_uniformint --> int
### hp_quniformint --> 
### hp_loguniform --> log double
### hp_qloguniform --> 
### hp_normal --> normal double
### hp_qnormal -->
### hp_lognormal --> 
### hp_qlognormal --> 

### 

### EXAMPLE
# space = hp.choice('a',
#     [
#         ('case 1', 1 + hp.lognormal('c1', 0, 1)),
#         ('case 2', hp.uniform('c2', -10, 10))
#     ])