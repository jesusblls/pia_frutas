import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk

# Función para cargar y predecir la imagen
def cargar_imagen():
    # Abrir cuadro de diálogo para seleccionar imagen
    file_path = filedialog.askopenfilename(title="Selecciona una imagen")
    
    if file_path:
        # Cargar y preparar la imagen
        img = image.load_img(file_path, target_size=(100, 100))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0  # Normalizar
        img_array = np.expand_dims(img_array, axis=0)  # Expandir para el modelo
        
        # Cargar el modelo entrenado
        model = tf.keras.models.load_model('modelo.h5')
        
        # Realizar la predicción
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)

        # Mapear la clase predicha a su etiqueta correspondiente
        print(predicted_class[0])
        class_labels = ['Uva en buen estado', 'Fresa en buen estado', 'Uva podrida', 'Fresa podrida', 'Manzana en buen estado', 'Banana en buen estado', 'Naranja en buen estado', 'Manzana podrida', 'Banana podrida', 'Naranja podrida']
        predicted_label = class_labels[predicted_class[0]]
        
        # Mostrar el resultado en la interfaz
        resultado_label.config(text=f"Resultado: {predicted_label}")
        
        # Mostrar la imagen en la interfaz
        img_display = Image.open(file_path)
        img_display = img_display.resize((200, 200))  # Redimensionar para que quepa en la interfaz
        img_tk = ImageTk.PhotoImage(img_display)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    else:
        resultado_label.config(text="No se seleccionó ninguna imagen.")

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Detección de Estado de Frutas")

# Establecer tamaño de la ventana y posición inicial
root.geometry("600x500")
root.resizable(width=True, height=True)

# Botón para cargar la imagen
boton_cargar = tk.Button(root, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(pady=20)

# Etiqueta para mostrar la imagen
image_label = Label(root)
image_label.pack()

# Etiqueta para mostrar el resultado
resultado_label = Label(root, text="Resultado: ", font=("Helvetica", 16))
resultado_label.pack(pady=20)

# Ejecutar la ventana
root.mainloop()
