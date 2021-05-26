import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from utils import load_galaxy_data
import app
from visualize import visualize_activations

input_data, labels = load_galaxy_data()

X_train, X_test, Y_train, Y_test = train_test_split(input_data, labels, test_size=0.2, random_state=222, stratify=labels)

train_data_generator = ImageDataGenerator(rescale=1.0/255.0)

batch_size_val = 5

train_iterator = train_data_generator.flow(X_train, Y_train, batch_size=batch_size_val)

validation_iterator = train_data_generator.flow(X_test, Y_test, batch_size=batch_size_val)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Input(shape=(128,128,3)))

model.add(tf.keras.layers.Conv2D(3, 3, strides=2, padding='valid', activation='relu'))

model.add(tf.keras.layers.Conv2D(8, 3, strides=2, padding='same', activation='relu'))

model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(4,activation="softmax"))

opt = tf.keras.optimizers.Adam(learning_rate=0.001)

loss_function = tf.keras.losses.CategoricalCrossentropy()

model.compile(

  loss=loss_function,

  optimizer=opt,

  metrics=[tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]

)

print(model.summary())

model.fit(

  train_iterator,

  steps_per_epoch = len(X_train)/batch_size_val,

  epochs=8,

  validation_data=validation_iterator,

  validation_steps=len(X_test)/batch_size_val

)

visualize_activations(model,validation_iterator)
