from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np

def genModel1(data):
    x = data[["Open", "High", "Low", "Volume"]]
    y = data["Close"]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.summary()
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(xtrain, ytrain, batch_size=1, epochs=30)
    scores = model.evaluate(xtest, ytest, verbose=0)
    print(scores)
    return model    
