"""

All the functions needed for algo trading

"""

import ccxt
import json
import pandas as pd
import numpy as np
#import dontshare_config as ds
from datetime import date, datetime, timezone, tzinfo
import time, schedule

ftx = ccxt.ftx({
    
    })
