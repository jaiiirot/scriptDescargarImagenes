from zipfile import ZipFile
from PIL import Image
import requests
from io import BytesIO

def descargar_imagenes_con_nombres(urls_con_nombres, ancho, alto):
    zip_filename = "imagenes.zip"
    with ZipFile(zip_filename, 'w') as zip:
        for obj in urls_con_nombres:
            response = requests.get(obj['image'])
            img = Image.open(BytesIO(response.content))
            img_resized = img.resize((ancho, alto))
            img_byte_array = BytesIO()
            img_resized.save(img_byte_array, format='PNG')
            img_data = img_byte_array.getvalue()
            filename = obj['title'] + '.png'
            zip.writestr(filename, img_data)

if __name__ == "__main__":
    urls_con_nombres = [
    {
        "image": "https://ejemplo.com/image.webp",
        "title": "nombre_de_la_imagen"
    }
]
    ancho = 250
    alto = 440
    descargar_imagenes_con_nombres(urls_con_nombres, ancho, alto)
