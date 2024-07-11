from PIL import Image
def encrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (b, g, r)

        img.save(output_path)
        print("Image encrypted successfully!")
        Image.open(output_path).show()
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (b, g, r)

        img.save(output_path)
        print("Image decrypted successfully!")
        Image.open(output_path).show()
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

input_image = r"M:\2024 installed program\python projects pycharm M\pythonProject\input.jpg"
encrypted_image = r"M:\2024 installed program\python projects pycharm M\pythonProject\encrypted.jpg"
decrypted_image = r"M:\2024 installed program\python projects pycharm M\pythonProject\decrypted.jpg"

encrypt_image(input_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)
