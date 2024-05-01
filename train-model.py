import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle
from joblib import dump

api_key = 'lAPjYCKxxlsCWu82hk5UkMJpU3w6xmAHG3SD7oTwtnIYy1sQ58Yeu5s1L4erJJ3E'
api_secret = 'u872WdYLmxJc8rgJhN6DAPiCI94UGJOEurhOFcWPBNFxEa03V8Txjl490lF5omB2'

df = pd.read_csv('./BTCUSDT_Historical_Data.csv')

df['Prev_Open'] = df['Open'].shift(1).astype(float)
df['Prev_Close'] = df['Close'].shift(1).astype(float)
df['Prev_Volume'] = df['Volume'].shift(1).astype(float)

df = df.dropna()

X = df[['Prev_Open', 'Prev_Close', 'Prev_Volume']]  
y = df[['Close']] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print(mse)


new_data = []

dump(model, '../predict.joblib')

