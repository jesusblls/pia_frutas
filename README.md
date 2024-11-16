# Clasificación de Frutas en Buen Estado o Mal Estado

Este proyecto de clasificación utiliza un modelo de aprendizaje profundo para determinar si una fruta se encuentra en buen estado o en mal estado. El proyecto consta de los siguientes componentes:

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de directorios y archivos:

- `test/`: Contiene imágenes de frutas en mal estado para el conjunto de prueba.
- `train/`: Contiene imágenes de frutas en buen estado para el conjunto de entrenamiento.
- `app.py`: Un script interactivo que permite al usuario seleccionar una imagen para ser clasificada por el modelo.
- `model.py`: Un script que genera y entrena el modelo de clasificación.
- `modelo.h5`: El modelo entrenado que se utiliza para realizar las predicciones.

## Cómo Utilizar la Aplicación

Para usar la aplicación de clasificación de frutas en buen estado o mal estado, sigue estos pasos:

1. Ejecuta el script `app.py`.
2. Se abrirá un cuadro de diálogo que te permitirá seleccionar una imagen de fruta que deseas clasificar.
3. Una vez que hayas seleccionado la imagen, el modelo la clasificará y te mostrará el resultado, indicando si la fruta está en buen estado o en mal estado.

## Entrenamiento del Modelo

El modelo de clasificación se encuentra en el archivo `model.py`. Utiliza un conjunto de datos que contiene imágenes de frutas en buen estado y mal estado para entrenar el modelo. El modelo se entrena durante 10 épocas y se guarda como `modelo.h5` para su uso posterior.

Asegúrate de tener los datos de entrenamiento en la estructura de directorios adecuada y que las imágenes tengan el tamaño correcto antes de entrenar el modelo.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar la aplicación:

- TensorFlow
- numpy
- tkinter (para la interfaz gráfica en `app.py`)

Para instalar las bibliotecas necesarias, puedes utilizar `pip`:

```bash
pip install tensorflow numpy
