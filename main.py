import SFunciones as SFu

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as pltcls

data = SFu.get_dataAV('AMZN', 'd', outputsize="compact")
print(data)

dataMOD = SFu.prepare_data(data)
print(dataMOD)