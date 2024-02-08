## Descargar Imágenes y Crear Archivo ZIP

Este script en Python te permite descargar imágenes desde URLs especificadas, redimensionarlas y guardarlas en un archivo ZIP con nombres personalizados.

### Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `requests`: Para realizar solicitudes HTTP y descargar las imágenes.
- `Pillow`: Para abrir, redimensionar y guardar las imágenes.

Puedes instalar las bibliotecas utilizando pip:

```bash
pip install requests Pillow
```

### Uso

1. Clona o descarga este repositorio en tu máquina local.

2. Asegúrate de tener el script Python `descargar_imagenes.py` en tu directorio de trabajo.

3. Abre el script y modifica la variable `urls_con_nombres` con las URLs de las imágenes que deseas descargar y sus respectivos títulos.

```python
urls_con_nombres = [
    {
        "image": "URL_de_la_imagen_1",
        "title": "Título_de_la_imagen_1"
    },
    {
        "image": "URL_de_la_imagen_2",
        "title": "Título_de_la_imagen_2"
    },
    # Agrega más imágenes según sea necesario
]
```

4. Configura las variables ancho y alto según las dimensiones deseadas para las imágenes redimensionadas.

```python
ancho = 250
alto = 440
```

5. Ejecuta el script Python utilizando el siguiente comando en tu terminal:

```bash
python descargar_imagenes.py
```

6. El script descargará las imágenes desde las URLs especificadas, las redimensionará y las guardará en un archivo ZIP llamado imagenes.zip.

### Notas

* Asegúrate de tener una conexión a Internet activa mientras ejecutas el script para descargar las imágenes.
* Verifica que las URLs de las imágenes sean válidas y accesibles.
* Las imágenes se guardarán con los nombres especificados en el archivo ZIP.

### ¡Disfruta descargando y redimensionando imágenes de forma fácil y rápida con este script Python!