from keras.layers import Dense, Dropout
from keras.models import Sequential
from numpy import genfromtxt

samples = genfromtxt('samples.csv', delimiter=',')
X = samples[:, 0:63]
Y = samples[:, 63]

# Create model
model = Sequential()
model.add(Dense(63, input_dim=63, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=100, validation_split=0.2, batch_size=4, shuffle=True, use_multiprocessing=True)

model.save("classifier.h5")
