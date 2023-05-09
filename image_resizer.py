# Programa para reescalar imágenes

from PIL import Image

image = Image.open("Nombre del archivo")

print(f"Tamaño actual: {image.size}")

resized_image = image.resize(
    ("Nuevo número(integer), nuevo número(integer)"))

resized_image.save("Nuevo nombre de la imagen")
