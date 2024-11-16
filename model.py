import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import scipy

# Directorios de los conjuntos de datos
train_dir = 'train'
test_dir = 'test'

# Preprocesamiento de imágenes
train_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(100, 100),  # Tamaño de las imágenes de entrada
    batch_size=32,
    class_mode='categorical'  # Clasificación categórica para múltiples clases
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(100, 100),
    batch_size=32,
    class_mode='categorical'
)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')  # 10 clases en total
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_generator, epochs=10, validation_data=test_generator)

model.save('modelo.h5')
