# Recurrent Neural Network



# Part 1 - Data Preprocessing

# Importing the libraries
import math
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.layers import Dropout
from keras import regularizers


# Importing the training set
df_trainSet = web.DataReader('AAPL', data_source = 'yahoo', start = '2019-01-01', end  = '2020-01-01')
df_testset = web.DataReader('AAPL', data_source = 'yahoo', start = '2020-01-01', end  = '2020-06-21')

df_trainSet = df_trainSet.dropna()
df_testset  = df_testset.dropna()
data = df_trainSet.iloc[:, 1:2].values
test_data = df_testset.iloc[:, 1:2].values

scaler = MinMaxScaler(feature_range = (0, 1))
scaled_train = scaler.fit_transform(data)


# Creating a data structure with 60 timesteps and 1 output
X_train = []
y_train = []
for i in range(60, 253):
    X_train.append(scaled_train[i-60:i, 0])
    y_train.append(scaled_train[i, 0])
    
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Part 2 - Building the RNN
# Initialising the RNN
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True, 
                   input_shape = (X_train.shape[1], 1), kernel_initializer="he_normal"))
regressor.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs = 1000, batch_size = 100)


# Part 3 - Making the predictions and visualising the results

# Getting the predicted stock price of 2017
dataset_total = pd.concat((df_trainSet['Open'], df_testset['Open']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(df_testset) - 50:].values
inputs = inputs.reshape(-1,1)
inputs = scaler.transform(inputs)
X_test = []
for i in range(60, 119):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

plt.plot(test_data, color = 'red', label = 'Real Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Stock Price')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()