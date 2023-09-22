import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Crear una ventana de tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal de tkinter

# Abrir un cuadro de diálogo para seleccionar una imagen
file_path = filedialog.askopenfilename(title="Selecciona una imagen")

if file_path:
    img = image.load_img(file_path, target_size=(100, 100))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalizar la imagen igual que durante el entrenamiento
    img_array = np.expand_dims(img_array, axis=0)  # Añadir una dimensión para formar un lote de una sola imagen

    # Cargar el modelo entrenado
    model = tf.keras.models.load_model('modelo.h5')

    # Realizar la predicción
    predictions = model.predict(img_array)

    # Obtener la clase con la probabilidad más alta como la predicción
    predicted_class = np.argmax(predictions, axis=1)

    # Mapear la clase predicha a su significado (por ejemplo, 'manzanas_buen_estado', 'manzanas_mal_estado', etc.)
    class_labels = ['freshapples', 'freshbanana', 'freshoranges', 'rottenapples', 'rottenbanana', 'rottenoranges']
    print(predicted_class)
    predicted_label = class_labels[predicted_class[0]]

    print(f"La imagen es clasificada como: {predicted_label}")
else:
    print("No se seleccionó ninguna imagen.")
