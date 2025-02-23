from PIL import Image
import sys

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Apply a simple mathematical operation to each pixel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    encrypted_image_path = image_path.replace(".", "_encrypted.")
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Reverse the mathematical operation to decrypt
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    decrypted_image_path = image_path.replace("_encrypted.", "_decrypted.")
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 image_encryptor.py <encrypt/decrypt> <image_path> <key>")
        sys.exit(1)

    operation = sys.argv[1]
    image_path = sys.argv[2]
    key = int(sys.argv[3])

    if operation == "encrypt":
        encrypt_image(image_path, key)
    elif operation == "decrypt":
        decrypt_image(image_path, key)
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
