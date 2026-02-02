from PIL import Image

def encrypt_decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # XOR operation
            r_new = r ^ key
            g_new = g ^ key
            b_new = b ^ key

            pixels[x, y] = (r_new, g_new, b_new)

    img.save(output_image)
    print(f"Image saved as {output_image}")

def main():
    key = 123  # Secret key (0–255)

    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        encrypt_decrypt_image("original.png", "encrypted.png", key)
        print("Encryption completed")
    elif choice == 2:
        encrypt_decrypt_image("encrypted.png", "decrypted.png", key)
        print("Decryption completed")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
