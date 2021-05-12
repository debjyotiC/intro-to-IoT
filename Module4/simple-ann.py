import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)  # i/p data
ys = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)  # labels

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])  # def NN
l1 = tf.keras.layers.Dense(units=6)
l2 = tf.keras.layers.Dense(units=6)
l3 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([l0, l1, l2, l3])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(xs, ys, epochs=150, verbose=True)

model.save('saved_model\\tf_model_2')

print("Weights are:{}".format(l0.get_weights()))
print("Weights are:{}".format(l1.get_weights()))
print("Weights are:{}".format(l2.get_weights()))

print(model.predict([100]))

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(history.history['loss'])
plt.show()
