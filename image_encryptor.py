from PIL import Image
import numpy as np
from tkinter import Tk, filedialog
import os

def encrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
        image_array = np.array(image).astype(np.uint16)

        encrypted_array = (image_array + key) % 256
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_image.save(output_path)
        print(f"Encrypted image saved as: {output_path}")
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
        image_array = np.array(image).astype(np.uint16)

        decrypted_array = (image_array - key) % 256
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_image.save(output_path)
        print(f"Decrypted image saved as: {output_path}")
    except Exception as e:
        print(f"Error decrypting image: {e}")

def choose_image_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return file_path

# choose Encryption key (between 1 and 255)
key = 50

# Select image file
image_path = choose_image_file()

if image_path and os.path.exists(image_path):
    # Generate output file names
    base_name, ext = os.path.splitext(os.path.basename(image_path))
    encrypted_path = f"{base_name}_encrypted.png"
    decrypted_path = f"{base_name}_decrypted.png"

    # Encrypt the image
    encrypt_image(image_path, key, encrypted_path)

    # Decrypt the image
    decrypt_image(encrypted_path, key, decrypted_path)
else:
    print("No image file selected")