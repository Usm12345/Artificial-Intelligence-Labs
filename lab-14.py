import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# Create synthetic dataset
np.random.seed(42)
X = np.random.rand(100, 1)
y = (X > 0.5).astype(int)

# Create the neural network model
model = Sequential()
model.add(Dense(4, activation='relu', input_shape=(1,)))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X, y, epochs=100, batch_size=16, validation_split=0.2)

# Plot the training history
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
