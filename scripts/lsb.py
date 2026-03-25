from PIL import Image

def extract_lsb(image_path, channels="RGB"):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bit_stream = ""

    for pixel in pixels:
        for i, ch in enumerate("RGBA"):
            if ch in channels and i < len(pixel):
                value = pixel[i]
                lsb = value & 1  
                bit_stream += str(lsb)


    message = ""
    for i in range(0, len(bit_stream), 8):
        byte = bit_stream[i:i+8]
        if len(byte) < 8:
            continue
        char = chr(int(byte, 2))
        message += char

    return message


if __name__ == "__main__":
    path = input("Enter PNG file path: ")
    
    print("\n--- Trying RGB ---")
    print(extract_lsb(path, "RGB")[:500])

    print("\n--- Trying RGBA ---")
    print(extract_lsb(path, "RGBA")[:500])

    print("\n--- Trying only R ---")
    print(extract_lsb(path, "R")[:500])
