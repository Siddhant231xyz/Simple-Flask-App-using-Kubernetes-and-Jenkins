import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Create and train a simple model
model = Sequential([
    Dense(128, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse')
X = np.array([[1], [2], [3], [4], [5]], dtype=float)
Y = np.array([[2], [4], [6], [8], [10]], dtype=float)

model.fit(X, Y, epochs=100)

# Save the model
model.save('simple_model.h5')
