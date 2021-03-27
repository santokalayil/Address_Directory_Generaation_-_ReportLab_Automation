import numpy as np
import pandas as pd
import warnings


def setView(max_rows=500,max_cols=500):
    pd.set_option('display.max_rows',max_rows)
    pd.set_option('display.max_columns',max_cols)
    np.set_printoptions(precision=3)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    np.random.seed(8)
    import warnings
    warnings.filterwarnings('ignore')


def widen():
    from IPython.core.display import display, HTML
    display(HTML("<style>.container { width:100% !important; }</style>"))


setView()
widen()

