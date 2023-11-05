

#Instalar estas librerías: pip install pillow pycryptodome numpy

# Parte 1

from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Cargar la imagen .bmp
image = Image.open('tux.bmp')

# Convertir la imagen en un arreglo NumPy
image_array = np.array(image)

# Redimensionar la imagen a 405x480x4
image_array = image_array.reshape(405, 480, 4)

# Generar una clave de 128 bits (16 bytes)
key = get_random_bytes(16)

# Generar un IV de 16 bytes
iv = get_random_bytes(16)

# Inicializar el cifrador AES en modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Cifrar los bytes de la imagen
ciphertext = cipher.encrypt(image_array.tobytes())

# Crear una nueva imagen a partir de los bytes cifrados
new_image = Image.frombytes('RGBA', (405, 480), ciphertext)

# Guardar la nueva imagen en formato PNG
new_image.save('result.png', 'PNG')

# Parte 2

# Cargar la imagen .bmp
image = Image.open('tux.bmp')

# Convertir la imagen en un arreglo NumPy
image_array = np.array(image)

# Redimensionar la imagen a 405x480x4
image_array = image_array.reshape(405, 480, 4)

# Generar una clave de 128 bits (16 bytes)
key = get_random_bytes(16)

# Inicializar el cifrador AES en modo ECB
cipher = AES.new(key, AES.MODE_ECB)

# Cifrar los bytes de la imagen
ciphertext = cipher.encrypt(image_array.tobytes())

# Crear una nueva imagen a partir de los bytes cifrados
new_image = Image.frombytes('RGBA', (405, 480), ciphertext)

# Guardar la nueva imagen en formato PNG
new_image.save('result_ecb.png', 'PNG')
