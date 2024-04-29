import pandas as pd;
import numpy as np;
from pandas_datareader.data import DataReader;

import matplotlib.pyplot as plt;

start_date = '2020-01-01';

end_date = '2023-06-01';

symbol = 'ETH-USD';

df = DataReader(name=symbol, data_source='yahoo', start=start_date, end=end_date);
df